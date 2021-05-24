# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2021-05-24

### Added

- CLI configuration can also be a YAML file

## [0.1.0] - 2021-05-21

### Added

- `assert-headers-py` CLI command for asserting a response against a header schema
- exports `assertHeaders` function for asserting a headers object against a schema
- exports `assertHeadersFromUrl` function which makes an HTTP(S) request and asserts the response headers against a configuration
