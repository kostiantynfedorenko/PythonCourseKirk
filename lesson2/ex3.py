'''
Read in the "show_arp.txt" file using the readlines() method. Use a list slice
 to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together
 as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named
"arp_entries.txt".
'''
from pprint import pprint

with open('show_arp.txt') as f:
    arp_output = f.readlines()

# Removed header line.
arp_output = arp_output[1:]
pprint(arp_output)

# Sort by IP addresses.
arp_output = sorted(arp_output, key=lambda x: x.split()[1])
# Commented line below sorts by MAC addresses.
# arp_output = sorted(arp_output, key=lambda x: x.split()[3])
# Get first 3 entries.
three_entries = arp_output[:3]
three_entries = '\n'.join(three_entries)

with open('arp_entries.txt', 'w') as f:
    f.write(three_entries)
