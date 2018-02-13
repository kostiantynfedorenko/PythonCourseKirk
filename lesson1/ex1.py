'''
Create a Python script that has three variables: ip_addr1, ip_addr2,
 ip_addr3 (representing three corresponding IP addresses). Print these
 three variables to standard output using a single print statement.

Make your print statement compatible with both Python2 and Python3.
'''
from __future__ import print_function

ip_addr1 = '1.1.1.1'
ip_addr2 = '2.2.2.2'
ip_addr3 = '3.3.3.3'

print('{} {} {}'.format(ip_addr1, ip_addr2, ip_addr3))
