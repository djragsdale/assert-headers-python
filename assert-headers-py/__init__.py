#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Classes
from AssertHeaders.HeaderAssertionError import HeaderAssertionError

# Functions in order they depend on each other
from AssertHeaders.getMeta import getMeta
from AssertHeaders.assertHeaders import assertHeaders
from AssertHeaders.assertHeadersFromUrl import assertHeadersFromUrl

# CLI Scripts
from AssertHeaders.cli import cli

if __name__ == '__main__':
    cli()