'''
1b. Expand on the ssh_conn function from exercise1 except add a fourth
 parameter 'device_type' with a default value of 'cisco_ios'. Print all four
 of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2
 function using the **kwargs technique.
'''
from __future__ import unicode_literals, print_function


def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print('#' * 80)
    print('IP Address: {}'.format(ip_addr))
    print('User Name: {}'.format(username))
    print('Password: {}'.format(password))
    print('Device type: {}'.format(device_type))
    print('*' * 80)


# Call without device type.
ssh_conn2('1.1.1.1', 'userA', 'passA')
# Call with device type.
ssh_conn2('1.1.1.1', 'userA', 'passA', device_type='cisco_nxos')
# Dict with parameters.
my_vars = {
    'ip_addr': '2.2.2.2',
    'username': 'userB',
    'password': 'passB',
    'device_type': 'cisco_iosxr'
}
# Call with dict.
ssh_conn2(**my_vars)
