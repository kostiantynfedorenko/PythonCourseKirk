'''
1a. Create an ssh_conn function. This function should have three parameters:
 ip_addr, username, and password. The function should print out each of these
 three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
'''
from __future__ import unicode_literals, print_function


def ssh_conn(ip_addr, username, password):
    print('#' * 80)
    print('IP Address: {}'.format(ip_addr))
    print('User Name: {}'.format(username))
    print('Password: {}'.format(password))
    print('#' * 80)


# Call using position.
ssh_conn('1.1.1.1', 'userA', 'passA')
# Call using named.
ssh_conn(ip_addr='2.2.2.2', password='passB', username='userB')
# Call using mix.
ssh_conn('3.3.3.3', username='userC', password='passC')
