import requests
r = requests.get("http://httpbin.org/headers") # get method
print(r.text)