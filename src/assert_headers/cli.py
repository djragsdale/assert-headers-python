import argparse
import os
import sys

from enum import Enum
from assert_headers import assertHeadersFromUrl, getMeta, HeaderAssertionError
from .get_cli_configuration import get_cli_configuration

class ExitCodes(Enum):
    ASSERTION_FAILED = 2
    CONFIGURATION_ERROR = 3
    SUCCESS = 0
    UNCAUGHT_ERROR = 1

def cli():
    meta = getMeta()

    if "--version" in sys.argv:
        print(f'assert-headers-py v{meta["__version__"]}')
        sys.exit(ExitCodes.SUCCESS.value)

    parser = argparse.ArgumentParser(
        prog = meta["__title__"],
        description = meta["__summary__"]
    )

    parser.add_argument("--config",
                        action="store",
                        help="Relative path to configuration file",
                        metavar="configurationPath",
                        type=str,
                        default="headersSchema.json")

    parser.add_argument("--silent",
                        action="store_const",
                        help="Don't output errors or headers",
                        const=True,
                        default=False)

    parser.add_argument("url",
                        action="store",
                        help="URL to retrieve headers from for assertion",
                        type=str)

    args = parser.parse_args()

    config = {}
    try:
        configuration_path = os.path.join(os.getcwd(), args.config)
        config = get_cli_configuration(configuration_path)
    except BaseException as err:
        if not args.silent:
            print(err)

        sys.exit(ExitCodes.CONFIGURATION_ERROR.value)

    headers = {}
    try:
        headers = assertHeadersFromUrl(args.url, config)

    except HeaderAssertionError as headerAssertionError:
        if not args.silent:
            print(headerAssertionError)

        sys.exit(ExitCodes.ASSERTION_FAILED.value)

    except BaseException as err:
        if not args.silent:
            print(err)

        sys.exit(ExitCodes.UNCAUGHT_ERROR.value)

    if not args.silent:
        print("assert-headers success\n")
        print(headers)

    sys.exit(ExitCodes.SUCCESS.value)

if __name__ == "__main__":
    cli()
