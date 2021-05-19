import os
import requests

from AssertHeaders import assertHeaders

def assertHeadersFromUrl(url, configuration):
    currentDir = os.path.realpath(os.path.join(os.path.dirname(__file__)))

    about = {}
    with open(os.path.join(currentDir, "__about__.py")) as f:
        exec (f.read(), about)

    currentVersion = about["__version__"]

    config = {
      "origin": "http://a.com",
      "userAgent": f'Assert Headers v{currentVersion} (https://github.com/djragsdale/assert-headers-python)',
      **configuration
    }

    res = requests.get(url, headers = {
      "origin": config["origin"],
      "user-agent": config["userAgent"]
    })

    assertHeaders(res.headers, configuration["schema"])

    return res.headers
