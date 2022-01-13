import requests
# https://www.sslproxies.org/

proxies = {
"http":"http://47.74.226.8:5001",
} 
r= requests.get("http://httpbin.org/ip",proxies=proxies)
print(r.text)