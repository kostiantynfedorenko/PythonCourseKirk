'''
Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list.
 Use the .extend() method to add two more IP addresses to the end of
 the list.

Use list concatenation to add two more IP addresses to the end of the
 list.

Print out the entire list of ip addresses. Print out the first IP
 address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and
 the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out
 the new first IP address in the list.
'''

from __future__ import print_function

ip_list = ['1.1.1.1', '20.20.20.20', '3.3.3.3', '4.4.4.4', '5.5.5.5']

print('{:20}{:50}'.format('Original list:', str(ip_list)))
ip_list.append('6.6.6.6')
print('{:20}{:50}'.format('Appended list:', str(ip_list)))
ip_list.extend(['7.7.7.7', '8.8.8.8'])
print('{:20}{:50}'.format('Extended list:', str(ip_list)))
ip_list = ip_list + ['9.9.9.9', '10.10.10.10']
print('{:20}{:50}'.format('Concatenated list:', str(ip_list)))
print('{:20}{:50}'.format('First address:', ip_list[0]))
print('{:20}{:50}'.format('Last address:', ip_list[len(ip_list) - 1]))
ip_list.pop(0)
ip_list.pop(len(ip_list) - 1)
print('{:20}{:50}'.format('POPed list:', str(ip_list)))
ip_list[0] = '2.2.2.2'
print('{:20}{:50}'.format('Updated list:', str(ip_list)))
