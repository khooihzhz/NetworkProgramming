# Modify the below code  to print the Content Type and  Character Set set of  "https://www.nav6.usm.my/contact-us/"
import requests 
 
url= "https://www.nav6.usm.my/contact-us/"

r=requests.get(url)
print(r.headers.get('Content-Type')) # get content type and charset     