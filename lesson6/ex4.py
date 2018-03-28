'''
4. Use send_config_set() and send_config_from_file() to make
 configuration changes.

The configuration changes should be benign. For example, on
 Cisco IOS I typically change the logging buffer size.

As part of your program verify that the configuration change
 occurred properly. For example, use send_command() to execute
  'show run' and verify the new configuration.
'''
from netmiko import Netmiko
from getpass import getpass


def output_wrapper(output, slogan, device):
    print('-' * 80)
    print(slogan.format(device))
    print('-' * 80)
    print('{}'.format(output))
    print('-' * 80)


command_set = ['logging console disable', 'logging buffered 10000']
command_sh_run = 'show run | in logging'
password = getpass()
my_device = {
    'host': '10.128.64.69',
    'username': 'admin',
    'password': password,
    'device_type': 'a10'
}
dev_conn = Netmiko(**my_device)

output_wrapper(dev_conn.send_command(command_sh_run),
               'Logging config on "{}" before changes:',
               my_device['host'])

changes = dev_conn.send_config_set(command_set)

output_wrapper(changes, 'Configured with set "{}":', my_device['host'])

output_wrapper(dev_conn.send_command(command_sh_run),
               'Logging config on "{}" after changes:',
               my_device['host'])

rev_changes = dev_conn.send_config_from_file('config.txt')

output_wrapper(rev_changes, 'Configured with file "{}":', my_device['host'])

output_wrapper(dev_conn.send_command(command_sh_run),
               'Logging config on "{}" after changes:',
               my_device['host'])
