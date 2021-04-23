'''

'''

from wsgiref.simple_server import make_server

from main import application

#############################################################

PORT = 8002
with make_server('', PORT, application) as httpd:
    print(f'Starting on port {PORT}...')
    httpd.serve_forever()
