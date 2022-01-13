import requests

url = "http://httpbin.org/post"

# post data
data = {
    'username': 'admin',
    'password': 'admin'
}

# proxy
proxies = {
"https":"https://47.243.121.143:59394",
} 

# setting header
headers = {
    'Content-type': 'application/pdf; charset=ISO-8859-1'
}

r = requests.post(url, data=data, proxies=proxies,headers=headers)

# response
print(r.text)