'''

'''
from dindondon_framework.templator import render


#############################################################################
class PcWelcome:
    def __call__(self, request):
        return '200 OK', [b'Welcome']


#############################################################################
class PcIndex:
    def __call__(self, request):
        return '200 OK', [render('index.html', data=request.get('data', None))]


#############################################################################
class PcAbout:
    def __call__(self, request):
        return '200 OK', [b'About']


#############################################################################
class PcInfo:
    def __call__(self, request):
        print(request)
        return '200 OK', [render('info.html', timestamp=request.get('timestamp', None))]

#############################################################################
