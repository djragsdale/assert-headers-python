import requests

from assert_headers import assertHeaders, getMeta

def assertHeadersFromUrl(url, configuration):
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
