from enum import Enum
from assert_headers import HeaderAssertionError

class ErrorTypes(Enum):
    FOUND_DISALLOWED = "found disallowed"
    INVALID_VALUE = "has invalid value for"
    MISSING_REQUIRED = "missing required"
    SCHEMA_ERROR = "invalid schema"

def assert_headers(headers, schema):
    errors = []

    for schemaHeader in schema:
        schemaValue = schema[schemaHeader]
        # schemaValue is False
        if not schemaValue:
            if schemaHeader in headers:
                errors.append({
                    "type": ErrorTypes.FOUND_DISALLOWED,
                    "headerName": schemaHeader,
                    "headerValue": headers[schemaHeader],
                    "message": f'"{schemaHeader}" is disallowed but was found'
                })
        # schemaValue is True
        elif schemaValue == True:
            if schemaHeader not in headers:
                errors.append({
                  "type": ErrorTypes.MISSING_REQUIRED,
                  "headerName": schemaHeader,
                  "message": f'"{schemaHeader}" is required but was missing'
                })
        # schemaValue is str
        elif isinstance(schemaValue, str):
            try:
                # Raises exception if key doesn't exist or if value is wrong
                assert(headers[schemaHeader] == schemaValue)
            except:
                errors.append({
                  "type": ErrorTypes.INVALID_VALUE,
                  "headerName": schemaHeader,
                  "message": f'"{schemaHeader}" expected value "{schemaValue}"'
                })
        # schemaValue is dict
        elif isinstance(schemaValue, dict):
            errorDict = {
                "type": ErrorTypes.INVALID_VALUE,
                "headerName": schemaHeader,
                "headerValue": headers[schemaHeader],
                "message": f'"{headers[schemaHeader]}" is not an allowed value for "{schemaHeader}"'
            }
            # if any are True, the header value must match a True schema value
            # if none are True, the header must NOT match a False schema value
            try:
                if True in schemaValue.values():
                    allowedValues = filter(lambda val: schemaValue[val] == True, [val for val in schemaValue])
                    if headers[schemaHeader] not in allowedValues:
                        errors.append(errorDict)
                else:
                    disallowedValues = [val for val in schemaValue]
                    if headers[schemaHeader] in disallowedValues:
                        errors.append(errorDict)
            except:
                  errors.append(errorDict)
        else:
            errors.append({
                "type": ErrorTypes.SCHEMA_ERROR,
                "headerName": schemaHeader,
                "message": f'the schema for "{schemaHeader}" is invalid'
            })
    
    if len(errors) > 0:
      raise HeaderAssertionError(errors)

    return True
