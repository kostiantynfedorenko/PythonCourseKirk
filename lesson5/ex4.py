'''
4. Copy your solution from exercise3 to exercise4. Add an 'import pdb' and
 pdb.set_trace() statement outside of your function (i.e. where you have your
  function calls).

Inside of pdb, experiment with:
Listing your code.
Using 'next' and 'step' to walk through your code. Make sure you understand
 the difference between next and step.
Experiment with 'up' and 'down' to move up and down the code stack.
Use p <variable> to inspect a variable.
Set a breakpoint and run your code to the breakpoint.
Use '!command' to change a variable (for example !new_mac = [])
'''
from __future__ import unicode_literals, print_function
import re
import pdb


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


pdb.set_trace()
print(mac_converter('00-00-aa-aa-bb-bb'))
print(mac_converter('0000.aaaa.bbbb'))
print(mac_converter('a:b:c:d:e:f'))
