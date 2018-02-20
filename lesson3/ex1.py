'''
Read the "show_vlan.txt" file into your program. Loop through the lines
 in this file and extract all of the VLAN_ID, VLAN_NAME combinations.
 From these VLAN_ID and VLAN_NAME construct a new list where each element
 in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this
 data structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
'''
from __future__ import unicode_literals, print_function
from pprint import pprint


with open('show_vlan.txt') as f:
    show_vlan = f.readlines()

output_list = []

for vlan_line in show_vlan:
    if vlan_line[0].isdigit():
        items = vlan_line.split()
        vlan = items[0]
        name = items[1]
        output_list.append((vlan, name))

# The same but using list comprehension
# output_list = [(x.split()[0], x.split()[1]) for x in show_vlan if
#     x.split()[0].isdigit()]

pprint(output_list)
