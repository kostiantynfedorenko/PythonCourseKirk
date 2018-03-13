'''
3. Similar to lesson3, exercise4 write a function that normalizes a MAC address
 to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from
 '00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return the
 normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
'''
from __future__ import unicode_literals, print_function
import re


def mac_converter(mac):
    mac = mac.upper()
    if re.search(r'[-:]', mac):
        new_mac = []
        octets = re.split(r"[-:]", mac)
        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)
    elif re.search(r'.*\..*', mac):
        new_mac = []
        sections = mac.split('.')
        if len(sections) != 3:
            raise ValueError("Invalid MAC address")
        for word in sections:
            if len(word) < 4:
                word = word.zfill(4)
            new_mac.append(word[:2])
            new_mac.append(word[2:])
    return ':'.join(new_mac)


print(mac_converter('00-00-aa-aa-bb-bb'))
print(mac_converter('0000.aaaa.bbbb'))
print(mac_converter('a:b:c:d:e:f'))
