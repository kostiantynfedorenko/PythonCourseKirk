'''
[Optional/bonus]

***
 Note, to actually test this in your environment, change the test IP
 addresses to something in your environment that you can ping successfully.
***

'''
from __future__ import unicode_literals, print_function
import subprocess
from subprocess import SubprocessError
from traceback import print_exc
import sys


# detect OS type based on user input, we expect 'l' or 'w'
os_type = sys.argv[1]

base_ip = '172.22.41.'
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
base_cmd = base_cmd_windows if os_type == 'w' else base_cmd_linux

ip_list = []
for last_octet in range(1, 255):
    new_ip = base_ip + str(last_octet)
    ip_list.append(new_ip)

for i, ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(i, ip_addr))

# Only use IP addresses X.X.X.100 to X.X.X.102
ip_list = ip_list[99:102]

print()
print('-' * 80)
for ip_addr in ip_list:
    print("IP Addr: ", ip_addr)
    print('-' * 80)
    cmd = base_cmd + ' ' + ip_addr
    try:
        output = subprocess.check_output(cmd.split())
        try:
            output = output.decode('utf-8')
        except (AttributeError) as e:
            print('Exception {} occured: "{}"'.format(type(e).__name__, e))
            print_exc()
        print(output)
    except SubprocessError as e:
        print('Exception {} occured: "{}"'.format(type(e).__name__, e))
        print_exc()
    print('-' * 80)
print('-' * 80)
print()
