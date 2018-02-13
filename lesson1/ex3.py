'''
Create three different variables the first variable should use all lower
 case characters with underscore ( _ ) as the word separator. The second
 variable should use all upper case characters with underscore as the word
 separator. The third variable should use numbers, letters, and underscore,
 but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are
 unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''
from __future__ import unicode_literals

ipv6_addr = '2001:10:8802:45ff::1'
IPV6_ADDR = '2001:10:8802:45ff::3'
ipv6_addr2 = '2001:10:8802:45ff::2'

print('-'*80)
print('Is variable1 equal to variable2: {}'.format(ipv6_addr == IPV6_ADDR))
print('Is variable1 not equal to variable2: {}'
      .format(ipv6_addr != ipv6_addr2))
print('-'*80)
