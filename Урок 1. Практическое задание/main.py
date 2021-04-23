'''

'''
import time
from datetime import date
from jinja2 import Template


#############################################################

def render(template_name, **kwargs):
    with open(template_name, encoding='utf-8') as f:
        template = Template(f.read())
    return bytes(template.render(**kwargs), 'utf-8')


#############################################################

class PcWelcome:
    def __call__(self, request):
        return '200 OK', [b'Welcome']


class PcIndex:
    def __call__(self, request):
        print('index call')
        print(request)
        return '200 OK', [b'Index']


class PcAbout:
    def __call__(self, request):
        return '200 OK', [b'About']


class PcInfo:
    def __call__(self, request):
        print(request)
        return '200 OK', [render('info.html', timestamp=request.get('timestamp', None))]


class PcDefault:
    def __call__(self, request):
        return '404 Not Found', [b'404 PAGE Not Found']


pc_list = {
    '/': PcWelcome(),
    '/index/': PcIndex(),
    '/about/': PcAbout(),
    '/info/': PcInfo(),
}


#############################################################
# Front controllers

def fc_base(request):
    print("fc_base")
    print(request)
    request['timestamp'] = time.time()
    request['data'] = date.today()  # time.time()


def fc_debug(request):
    print("fc_debug")
    if True:
        request['debug'] = True


fc_list = [fc_base,
           fc_debug]


#############################################################
class Application:

    def __init__(self, pc_list, fc_list):
        self.pc_list = pc_list
        self.fc_list = fc_list

    def __call__(self, environ, start_response):
        # setup_testing_defaults(environ)
        print(f"{environ['PATH_INFO']} requested")
        path = environ['PATH_INFO']
        if path[-1] != '/':
            path = path + '/'
        if path in self.pc_list:
            view = self.pc_list[path]
        else:
            view = PcDefault()
        request = {}
        # front controller
        for front in self.fc_list:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body


#############################################################
application = Application(pc_list, fc_list)
