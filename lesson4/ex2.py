'''
Create three separate lists of IP addresses. The first list should be the IP
 addresses of the Houston data center routers, and it should have over ten
 RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers,
 and it should have at least eight RFC1918 IP addresses (including some
 addresses that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers,
 and it should have at least eight RFC1918 IP addresses. The Chicago IP
 addresses should have some overlap with both the IP addresses in Houston and
 Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between
 Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three
 sites.

Using set operations, find the IP addresses that are entirely unique in
 Chicago.
'''
from __future__ import unicode_literals, print_function


def print_banner():
    print('#' * 80)


houston_ips = [
    '192.168.1.1',
    '192.168.2.1',
    '192.168.3.1',
    '192.168.4.1',
    '192.168.5.1',
    '192.168.6.1',
    '192.168.7.1',
    '192.168.8.1',
    '192.168.1.1',
    '192.168.2.1',
    '192.168.7.1'
]
atlanta_ips = [
    '192.168.1.1',
    '192.168.2.1',
    '192.168.3.1',
    '192.168.104.1',
    '192.168.105.1',
    '192.168.106.1',
    '192.168.107.1',
    '192.168.108.1'
]
chicago_ips = [
    '192.168.1.1',
    '192.168.2.1',
    '192.168.104.1',
    '192.168.105.1',
    '192.168.21.1',
    '192.168.22.1',
    '192.168.23.1',
    '192.168.24.1'
]
houston_ips = set(houston_ips)
atlanta_ips = set(atlanta_ips)
chicago_ips = set(chicago_ips)
print_banner()
print("Duplicate IPs at Houston and Atlanta sites:\n\n{}".
      format(houston_ips & atlanta_ips))
print_banner()
print("Duplicate IPs at all three sites:\n\n{}".
      format(houston_ips & atlanta_ips & chicago_ips))
print_banner()
print("Chicago unique IP addresses:\n\n{}".format(
        chicago_ips.difference(houston_ips).difference(atlanta_ips)))
print_banner()
