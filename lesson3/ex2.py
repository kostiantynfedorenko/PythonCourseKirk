'''
Read the contents of the "show_arp.txt" file. Using a for loop, iterate
 over the lines of this file. Process the lines of the file and separate
 out the ip_addr and mac_addr for each entry into a separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1
 is found, print out the string "Default gateway IP/Mac" and the
 corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP
 address is found, then print out "Arista3 IP/Mac is" and the corresponding
 ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3
 switch. Once you have found both of these devices, 'break' out of the for
 loop.
'''
from __future__ import unicode_literals, print_function


DEF_GW = '10.220.88.1'
ARISTA3_IP = '10.220.88.30'

with open('show_arp.txt') as f:
    show_arp = f.readlines()

found_gw, found_arista3 = (False, False)

for line in show_arp:
    if 'Protocol' in line:
        continue
    items = line.split()
    ip_address = items[1]
    mac_address = items[3]
    if ip_address == DEF_GW:
        print('Default gateway {}/{}'.format(ip_address, mac_address))
        found_gw = True
    elif ip_address == ARISTA3_IP:
        print('Arista3 IP/Mac is {}/{}'.format(ip_address, mac_address))
        found_arista3 = True
    if found_gw and found_arista3:
        print('Hit break')
        break
