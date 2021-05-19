
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_assertHeadersFromUrl
----------------------------------
Tests for `AssertHeaders` module.
"""

import pytest
from mock import patch
import unittest

from AssertHeaders import assertHeadersFromUrl, HeaderAssertionError

class AssertHeadersTest(unittest.TestCase):
  def test_raises_if_request_fails_header_assertion(self):
      config = {
          "schema": {
              "x-content-type-options": "nosniff"
          }
      }
      url = "https://example.com"

      with patch("requests.get") as mock_request:
          mock_request.return_value.status_code = 200
          mock_request.return_value.headers = {
              "content-type": "text/html"
          }

          with self.assertRaises(HeaderAssertionError):
              assertHeadersFromUrl(url, config)

  def test_returns_headers_on_valid_http_response_headers(self):
      config = {
          "schema": {
              "x-content-type-options": "nosniff"
          }
      }
      url = "https://example.com"

      with patch("requests.get") as mock_request:
          mock_request.return_value.status_code = 200
          mock_request.return_value.headers = {
              "content-type": "text/html",
              "x-content-type-options": "nosniff"
          }

          self.assertEqual(type(assertHeadersFromUrl(url, config)), dict)