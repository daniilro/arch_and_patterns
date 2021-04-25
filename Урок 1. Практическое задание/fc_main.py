'''

'''
import time
from datetime import date

from views import PcWelcome, PcIndex, PcAbout, PcInfo, PcNotFound


# Front controllers
#############################################################
def fc_base(request):
    print("fc_base")
    print(request)
    request['timestamp'] = time.time()
    request['data'] = date.today()


def fc_debug(request):
    print("fc_debug")
    if True:
        request['debug'] = True
    request['key'] = 'key'


fc_list = [fc_base,
           fc_debug]

#############################################################
