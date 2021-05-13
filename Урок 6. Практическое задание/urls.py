'''

'''
import time
from datetime import date


# Front controllers
#############################################################
def fc_base(request):
    print("fc_base")
    request['timestamp'] = time.time()
    request['date'] = date.today()


#############################################################
def fc_debug(request):
    print("fc_debug")
    if True:
        request['debug'] = True
    request['key'] = 'key'


#############################################################
fc_list = [fc_base,
           fc_debug]

#############################################################
