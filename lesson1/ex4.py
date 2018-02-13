'''
Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
'''
from __future__ import print_function

show_version = '*0        CISCO881-SEC-K9       FTX0000038X    '

show_version = show_version.strip()
show_v_lst = show_version.split()
print('-'*80)
print('Show version string: "{}"'.format(show_version))
print('Is "Cisco" in show version: {}'
      .format('cisco' in show_v_lst[1].lower()))
print('Is "881" in show version: {}'.format('881' in show_v_lst[1]))
print('SN: {:^15}Model: {:^15}'.format(show_v_lst[2], show_v_lst[1]))
print('-'*80)
