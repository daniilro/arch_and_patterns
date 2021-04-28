'''

'''
from dindondon_framework.templator import render

TEMPLATES_FOLDER = 'templates'


#############################################################################
class PcWelcome:
    def __call__(self, request):
        return '200 OK', [
            render(
                'contact.html', folder=TEMPLATES_FOLDER, data=request.get(
                    'data', None))]


#############################################################################
class PcIndex:
    def __call__(self, request):
        return '200 OK', [
            render(
                'index.html', folder=TEMPLATES_FOLDER, data=request.get(
                    'data', None))]


#############################################################################
class PcAbout:
    def __call__(self, request):
        return '200 OK', [
            render(
                'about.html', folder=TEMPLATES_FOLDER, data=request.get(
                    'data', None))]


#############################################################################
class PcInfo:
    def __call__(self, request):
        print(request)
        return '200 OK', [
            render(
                'info.html', folder=TEMPLATES_FOLDER, timestamp=request.get(
                    'timestamp', None))]


#############################################################################
class PcContact:
    def __call__(self, request):
        return '200 OK', [
            render(
                'contact.html', folder=TEMPLATES_FOLDER, data=request.get(
                    'data', None))]


#############################################################################
class PcFeedback:
    def __call__(self, request):
        return '200 OK', [
            render(
                'feedback.html', folder=TEMPLATES_FOLDER, data=request.get(
                    'data', None))]


#############################################################################
pc_list = {
    '/': PcIndex(),  # PcWelcome(),
    '/index/': PcIndex(),
    '/about/': PcAbout(),
    '/info/': PcInfo(),
    '/feedback/': PcFeedback(),
}

#############################################################
