'''
Read in the "show_ip_int_brief.txt" file into your program using the
 .readlines() method.

Obtain the list entry associated with the FastEthernet0/1 interface. You
 can just hard-code the index at this point since we haven't covered
 for-loops or regular expressions. Use the string .split() method to
 obtain both the IP address and the corresponding name associated
 with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero. You
 might need to 'pip install pycodestyle' on your computer (you should
 be able to type this from the shell prompt). Alternatively, you can
 type 'python -m pip install pycodestyle'.
'''

with open('show_ip_int_brief.txt') as f:
    int_output = f.readlines()

int_fa01 = int_output[2].strip()
ip_address = int_fa01.split()[1]
intf_name = int_fa01.split()[0]

fa01_tpl = (intf_name, ip_address)

print(fa01_tpl)
