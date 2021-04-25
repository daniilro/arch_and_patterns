'''

'''

#############################################################################


class Framework:

    def __init__(self, pc_list, fc_list):
        self.pc_list = pc_list
        self.fc_list = fc_list

    def __call__(self, environ, start_response):
        print(f"{environ['PATH_INFO']} requested")
        path = environ['PATH_INFO']
        # page controller ###########################################
        if not path.endswith('/'):
            path += '/'
        if path in self.pc_list:
            view = self.pc_list[path]
        else:
            view = self.pc_list['notfound']
        request = {}
        # front controller ###########################################
        for front in self.fc_list:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body

#############################################################################
