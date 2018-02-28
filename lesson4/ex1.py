'''
Create a dictionary representing a network device. The dictionary should have
 key-value pairs representing the 'ip_addr', 'vendor', 'username', and
 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the
 'vendor' key is 'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary
 should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value
 pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the
 dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the
 dictionary keys and values.
'''
from __future__ import unicode_literals, print_function

net_device = {'ip_addr': '1.1.1.1', 'vendor': 'cisco', 'username': 'userA',
              'password': 'passA'}

print(net_device['ip_addr'])

# net_device['platform'] = 'ios' if net_device['vendor'] == 'cisco' else
# 'junos'

if net_device['vendor'] == 'cisco':
    net_device['platform'] = 'ios'
elif net_device['vendor'] == 'juniper':
    net_device['platform'] = 'junos'

bgp_fields = {'bgp_as': '65001', 'peer_as': '65003', 'peer_ip': '2.2.2.2'}

net_device.update(bgp_fields)

for key in net_device:
    print(key)

for k, v in net_device.items():
    print('{:^20} --> {:^20}'.format(k, v))
