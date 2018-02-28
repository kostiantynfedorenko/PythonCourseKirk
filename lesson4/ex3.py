'''
Read in the 'show_version.txt' file. From this file, use regular expressions
 to extract the OS version, serial number, and configuration register values.

Your output should look as follows:
OS Version: 15.4(2)T1
Serial Number: FTX0000038X
​Config Register: 0x2102
'''
from __future__ import unicode_literals, print_function
import re

with open('show_version.txt') as f:
    output = f.read()

resultdict = {}

resultdict.update(re.search(r'Cisco.+Version\s(?P<version>.+),', output,
                            flags=re.M).groupdict())
resultdict.update(re.search(r'Processor board ID\s(?P<serial_num>.+)', output,
                            flags=re.M).groupdict())
resultdict.update(re.search(r'Configuration register is\s(?P<conf_reg>.+)',
                            output, flags=re.M).groupdict())

print('OS Version: {}'.format(resultdict['version']))
print('Serial Number: {}'.format(resultdict['serial_num']))
print('​Config Register: {}'.format(resultdict['conf_reg']))
