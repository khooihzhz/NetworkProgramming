# changing compression scheme from gzip to brotli

import requests

headers = {
    "Accept-Encoding": "br"     # short form for brotli
}

r = requests.get("http://httpbin.org/headers", headers=headers) # get method
print(type(r.headers['accept-encoding']))