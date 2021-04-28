'''

'''

from wsgiref.simple_server import make_server
from dindondon_framework.main import Framework
from urls import pc_list, fc_list

#############################################################
application = Framework(pc_list, fc_list)
#############################################################
PORT = 8000
with make_server('', PORT, application) as httpd:
    print(f'Starting on port {PORT}...')
    httpd.serve_forever()
