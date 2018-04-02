'''
1a. Use Jinja2 templating to render the following:
vlan
   name

Your template should be inside of your Python program for simplicity.

The output from processing your template should be as follows. This
 should be printed to stdout.
vlan 400
   name red400
'''
from __future__ import unicode_literals, print_function
import jinja2


templ = '''

vlan {{ vlan_id }}
   name {{ vlan_name }}

'''

vlan_vars = {
    'vlan_id': 400,
    'vlan_name': 'red400'
}

t = jinja2.Template(templ)
print(t.render(vlan_vars))
