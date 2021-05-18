
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_assertHeaders
----------------------------------
Tests for `AssertHeaders` module.
"""

import pytest
import unittest

from AssertHeaders.assertHeaders import assertHeaders
from AssertHeaders.HeaderAssertionError import HeaderAssertionError

baseSchema = {
    "cache-control": False,
    "strict-transport-security": True,
    "x-content-type-options": "nosniff",
    "x-frame-options": {
        # if any are True, the header value must match a True schema value
        "DENY": True,
        # if none are true, the header must NOT match a false schema value
        "SAMEORIGIN": False
    }
}

baseHeaders = {
    "strict-transport-security": "max-age=31536000; includeSubDomains",
    "x-content-type-options": "nosniff",
    "x-frame-options": "DENY"
}

class AssertHeadersTest(unittest.TestCase):
    def test_errors_on_missing_required_header(self):
        headers = {**baseHeaders}
        headers.pop("strict-transport-security")
        schema = {**baseSchema}
        with self.assertRaises(HeaderAssertionError):
            assertHeaders(headers, schema)

    def test_passes_on_presence_of_required_header(self):
        headers = {
          **baseHeaders,
          "strict-transport-security": "abcd"
        }
        schema = {**baseSchema}
        # shouldn't throw
        assertHeaders(headers, schema)

    def test_errs_on_presence_of_excluded_header(self):
        headers = {
          **baseHeaders,
          "cache-control": "abcd"
        }
        schema = {**baseSchema}
        with self.assertRaises(HeaderAssertionError):
            assertHeaders(headers, schema)

    def test_passes_on_missing_excluded_header(self):
        headers = {**baseHeaders}
        self.assertFalse(hasattr(headers, "cache-control"))
        schema = {**baseSchema}
        # shouldn't throw
        assertHeaders(headers, schema)

    def test_errs_for_presence_of_disallowed_header_value(self):
        headers = {
          **baseHeaders,
          "x-frame-options": "SAMEORIGIN"
        }
        schema = {**baseSchema}
        with self.assertRaises(HeaderAssertionError):
            assertHeaders(headers, schema)

    def test_errs_for_presence_of_missing_header_value(self):
        headers = {
          **baseHeaders,
          "x-frame-options": "ALLOW-FROM eaxmple.com"
        }
        schema = {**baseSchema}
        with self.assertRaises(HeaderAssertionError):
            assertHeaders(headers, schema)

    def test_passes_for_allowed_header_value(self):
        headers = {
          **baseHeaders,
          "x-frame-options": "DENY"
        }
        schema = {**baseSchema}
        # shouldn't throw
        assertHeaders(headers, schema)

    def test_reports_multiple_errors(self):
        headers = {
          **baseHeaders,
          "cache-control": "abcd",
          "x-content-type-options": "abcd",
          "x-frame-options": "SAMEORIGIN"
        }
        headers.pop("strict-transport-security")
        schema = {**baseSchema}

        try:
            assertHeaders(headers, schema)
            self.assertTrue(False) # Should not get reached
        except HeaderAssertionError as errs:
            self.assertEqual(len(errs.errors), 4)
            for err in errs:
                self.assertTrue(hasattr(err, "type"))
                self.assertTrue(hasattr(err, "headerName"))
                self.assertTrue(hasattr(err, "message"))
