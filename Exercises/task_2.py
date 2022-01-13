from http import server
from wsgiref.simple_server import make_server

# simple web app
def web_app (environ, start_response):
    status ="200 Ok"
    headers=[('content-type','text/html; charset=utf-8')]
    start_response(status,headers)
    return [b'<img src="https://www.pinclipart.com/picdir/middle/55-552426_python-sticker-png-clipart.png">']

# Server 
with make_server('',9000,web_app) as server:
    print("server started ...")
    server.serve_forever()
