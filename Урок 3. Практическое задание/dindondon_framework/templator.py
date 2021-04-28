'''

'''

import os

#from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


#############################################################
def render(template_name, folder='templates', **kwargs):

    env = Environment()
    env.loader = FileSystemLoader(folder)

    template = env.get_template(template_name)

    return bytes(template.render(**kwargs), 'utf-8')

#    file_path = os.path.join(folder, template_name)
#    with open(file_path, encoding='utf-8') as f:
#        template = Template(f.read())
#    return bytes(template.render(**kwargs), 'utf-8')

#############################################################
