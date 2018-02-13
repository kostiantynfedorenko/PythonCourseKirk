'''
Prompt a user to enter in an IP address from standard input. Read the IP
 address in and break it up into its octets. Print out the octets in decimal,
 binary, and hex.
Your program output should look like the following:
​ $ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------
Four columns, fifteen characters wide, a header column, data centered in the
 column.
'''

from __future__ import print_function

try:
    ip_address = raw_input('Please enter an IP address: ')
except NameError:
    ip_address = input('Please enter an IP address: ')

octets = ip_address.split('.')
octets_int = [int(x) for x in octets]
print('{:^15}{:^15}{:^15}{:^15}'
      .format('Octet1', 'Octet2', 'Octet3', 'Octet4'))
print('-' * 80)
print('{:^15}{:^15}{:^15}{:^15}'.format(*octets))
print('{:^15}{:^15}{:^15}{:^15}'.format(bin(octets_int[0]), bin(octets_int[1]),
      bin(octets_int[2]), bin(octets_int[3])))
print('{:^15}{:^15}{:^15}{:^15}'.format(hex(octets_int[0]), hex(octets_int[1]),
      hex(octets_int[2]), hex(octets_int[3])))
print('-' * 80)
print()
