'''

'''

from wsgiref.simple_server import make_server

from dodo_framework.dodo_main import Framework
from fc_main import fc_list
from pc_main import pc_list

#############################################################
application = Framework(pc_list, fc_list)
#############################################################
PORT = 8000
with make_server('', PORT, application) as httpd:
    print(f'Starting on port {PORT}...')
    httpd.serve_forever()
