'''
[Optional/bonus]

***
 Note, to actually test this in your environment, change the test IP
 addresses to something in your environment that you can ping successfully.
***

'''
from __future__ import unicode_literals, print_function
import re

with open('show_ipv6_intf.txt') as f:
    output_ipv6 = f.read()

matches = re.search(r'IPv6 address:\s+(.*)\s+\sIPv6 subnet:', output_ipv6,
                    flags=re.DOTALL)
ipv6_lines = matches.group(1).splitlines()
ipv6_addresses = []
for line in ipv6_lines:
    address = re.sub(r'\[VALID\]', '', line)
    ipv6_addresses.append(address.strip())
print(ipv6_addresses)
