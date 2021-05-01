'''

'''

import quopri

from dindondon_framework.requestor import GetRequests, PostRequests


#############################################################################
class PcDefault:
    def __call__(self, request):
        return '404 Not Found', [b'404 PAGE Not Found']


#############################################################################

class Framework:

    def __init__(self, pc_list, fc_list):
        self.pc_list = pc_list
        self.fc_list = fc_list

    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'

        request = {}

        method = environ['REQUEST_METHOD']
        print(f"REQUEST_METHOD = \'{method}\'")
        print(f"QUERY_STRING = \'{environ['QUERY_STRING']}\'")

        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'---\nPOST request received.\nParameters:')
            for r in Framework.decode_value(data).items():
                print(f'{r[0]}\t= {r[1]}')
            print(f'---\n')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'---\nGET request received.\nParameters:')
            for r in request['request_params']:
                print(f"{r}={request['request_params'][r]}")
            print(f'---\n')

        if path in self.pc_list:
            view = self.pc_list[path]
        else:
            view = PcDefault()
        print(f"\'{environ['PATH_INFO']}\' requested")

        # front controller
        for front in self.fc_list:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
