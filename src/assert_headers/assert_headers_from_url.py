import requests

from assert_headers import assert_headers, get_meta

def assert_headers_from_url(url, configuration):
    meta = getMeta()

    config = {
      "origin": "http://a.com",
      "userAgent": f'Assert Headers v{meta["__version__"]} ({meta["__uri__"]})',
      **configuration
    }

    res = requests.get(url, headers = {
      "origin": config["origin"],
      "user-agent": config["userAgent"]
    })

    assertHeaders(res.headers, configuration["schema"])

    return res.headers
