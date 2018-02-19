'''
Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP
 output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local
 AS number.

From the last line use the string .split() method to obtain the BGP peer
 IP address.

Print both local AS number and the BGP peer IP address to the screen.
'''

with open('show_ip_bgp_summ.txt') as f:
    output = f.readlines()

first_line = output[0]
last_line = output[len(output) - 1]
as_num = first_line.split()[len(first_line.split()) - 1]
peer_ip_address = last_line.split()[0]
print('{:20}||{:^20}'.format('LOCAL AS', 'PEER IP'))
print('='*40)
print('{:20}||{:^20}'.format(as_num, peer_ip_address))
