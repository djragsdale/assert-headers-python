# assert_headers

Assert HTTP headers

## Usage

### CLI

#### Global usage

```bash
pip install assert_headers
# Assume headersSchema.json in current working directory
assert-headers-py https://example.com
```

or with specified configuration

```bash
assert-headers-py --config ./customConfiguration.json https://example.com
```

in silent mode

```bash
assert-headers-py --silent --config ./customConfiguration.json https://example.com
```

to see what version you are running

```bash
assert-headers-py --version
```

##### Advanced CLI Usage

TODO: Add example of how to stream a column of a .csv into the tool

TODO: Show how the exit codes can be used in smoke tests

#### CLI Configuration

`assert-headers-py` currently accepts configuration in JSON or YAML formats. It allows specifying a schema for the headers, but also the outgoing origin and user-agent headers for the request. Below is an example configuration:

```json
{
  "userAgent": "assert-headers-py",
  "origin": "https://example.com",
  "schema": {
    "cache-control": false,
    "strict-transport-security": true,
    "x-content-type-options": "nosniff",
    "x-frame-options": {
      "DENY": true,
      "SAMEORIGIN": false
    }
  }
}
```

```yaml
userAgent: "assert-headers-py"
origin: "https://example.com"
schema:
  cache-control: False
  strict-transport-security: True
  x-content-type-options: "nosniff"
  x-frame-options:
    DENY: True
    SAMEORIGIN: False
```

**Schema Explanation:**

> Note: Since the example format of the schema is JSON, the values will use `false` instead of `False` and `true` instead of `True`.

1. `"disallowed-header-name": false` - It is considered an error if this header is defined
1. `"required-header-name": true` - It is considered an error if this header is missing (or `undefined`)
1. `"strict-header-name": "only good value"` - It is considered an error if this header does not have this value
1. `"enumerated-header-name": { "good header value": true, "another good value": true }` - It is considered an error if this header contains a value other than one marked `true`.
1. `"enumerated-header-name": { "bad header value": false, "another bad value": false }` - It is considered an error if this header contains a value not marked `true`
1. If no enumerated header values are marked `true`, all listed values are considered invalid values. It is highly recommended to ONLY use `true` and `false` for enumerated values

### assertHeader

```python
from assert_headers import assertHeader

headers = {
  "strict-transport-security": "max-age=31536000; includeSubDomains",
  "x-content-type-options": "nosniff",
  "x-frame-options": "DENY"
}
schema = {
  "cache-control": False,
  "strict-transport-security": True,
  "x-content-type-options": "nosniff",
  "x-frame-options": {
    # if any are true, the header value must match a true schema value
    "DENY": True
  }
}

try:
  assertHeaders(headers, schema)
except BaseException as err:
  print("OOPS!")
  print(err.message)
  if err.errors:
    for assertionError in err.errors:
      print(f'The header {assertionError.headerName} was bad!')
```

This can also be used inside a test library for validating HTTP response headers.

### assertHeaderFromUrl

```python
from assert_headers import assertHeaderFromUrl

configuration = {
  "userAgent": "Custom User Agent name",
  "origin": "https://my-domain.com",
  "schema": {
    "cache-control": False,
    "strict-transport-security": True,
    "x-content-type-options": "nosniff",
    "x-frame-options": {
      # if any are true, the header value must match a true schema value
      "DENY": True
    }
  }
}

assertHeaderFromUrl("https://example.com/my-test-page", configuration)
```

## Contributing

```bash
# 1. Install Poetry
# 2. Install dependencies
poetry install
# 3. Start contained environment
poetry shell
# 3 (alternate). Run virtualenv inside current shell
# source ./venv/bin/activate
# 4. Make changes
# 5. Run tests
poetry run pytest
```

If installing additional dependencies:

```bash
# Inside Poetry shell or virtualenv/venv
poetry add my_new_package
```

For more information, refer to https://python-poetry.org/docs/basic-usage/.
