'''
3. Find a command on your device that has additional prompting.
 Use send_command_timing to send the command down the SSH channel.
 Capture the output and handle the additional prompting.
'''
from netmiko import Netmiko
from getpass import getpass


command = 'no partition testP id 1'
password = getpass()
my_device = {
    'host': '10.128.64.69',
    'username': 'admin',
    'password': password,
    'device_type': 'a10'
}
dev_conn = Netmiko(**my_device)
dev_conn.config_mode()
print('Prompt for device {} is: {}'.format(my_device['host'],
                                           dev_conn.find_prompt()))
com_output = dev_conn.send_command_timing(command)
if 'Remove this partition' in com_output:
    com_output += dev_conn.send_command_timing('y\n')

print('*' * 80)
print('Output of "{}" command on "{}"'.format(command, my_device['host']))
print('*' * 80)
print('{}'.format(com_output))
print('*' * 80)
