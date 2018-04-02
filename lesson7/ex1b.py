'''
1b. Using a conditional in a Jinja2 template, generate the following output:
crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic

The encryption of aes, and the Diffie-Hellman group should be variables in
 the template.

Additionally this entire ISAKMP section should only be added if the
 isakmp_enable variable is set to True.

Your template should be inside your Python program for simplicity.
'''
from __future__ import unicode_literals, print_function
import jinja2


crypto_templ = '''

crypto isakmp policy 10
 encr {{ encryption }}
 authentication pre-share
 group {{ dh_group }}
{% if isakmp_enable -%}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{% endif %}

'''

crypto_vars = {
    'encryption': 'aes',
    'dh_group': 5,
    'isakmp_enable': True
}

t = jinja2.Template(crypto_templ)
print(t.render(crypto_vars))
