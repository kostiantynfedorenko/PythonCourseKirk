'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of
 this file. Keep reading the lines until you have encountered the remote
 "System Name" and remote "Port id". Save these two items into variables
 and print them to the screen. You should extract only the system name
 and port id from the lines (i.e. your variables should only have
 'twb-sf-hpsw1' and '15'). Break out of your loop once you have retrieved
 these two items.
'''
from __future__ import unicode_literals, print_function

with open('show_lldp_neighbors_detail.txt') as f:
    lldp_output = f.readlines()

for line in lldp_output:
    if 'Port id' in line:
        _, port_id = line.strip().split('Port id: ')
    elif 'System Name' in line:
        _, system_name = line.strip().split('System Name: ')
    if 'port_id' in locals() and 'system_name' in locals():
        print('Port id: {:^5}|| System Name: {:^10}'
              .format(port_id, system_name))
        break
