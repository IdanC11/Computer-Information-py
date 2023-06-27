# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:04:37 2022

@author: edanc
"""

import re
import subprocess
# tables library
from tabulate import tabulate

def run_command(cmd):
    return subprocess.Popen(cmd,
                            shell=True, # not recommended, but does not open a window
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE).communicate()

# regex pattern for multiple options
def pattern(item, groupNum):
    temp = []
    pattern_Item = re.compile(item)
    find_Item = pattern_Item.finditer(output)
    for match in find_Item:
        temp.append(match.group(groupNum))
       
    return temp

# decode byte stream to utf-8 string format
output = (run_command('ipconfig /all')[0]).decode('utf-8')
# get rid of 'cursor return' chars
output = re.sub(r'\r', r'', output)

# get adapter names
final_Adapters = pattern(r'(.*? adapter .*)(:)', 1)
# get DHCP enabled flag
final_DHCP = pattern(r'DHCP Enabled(. )+: (Yes|No)', 2)
# get Physical address
final_PHA = pattern(r'Physical Address(. )+: ((\w\w-){5}\w\w)', 2)
# get media state
final_State = []
for adapter in final_Adapters:
    # treat special case, when there is a '*' inside the adapter name
    m = re.search(r'[*]', adapter)
    if m != None:
        adapter = re.sub(r'[*]', r'[*', adapter) + r']+'
    result = pattern(adapter + r':(\n\n.*?)(Media)(.*?):(.*?)(\n)', 4)
    state = 'Unknown'
    if result != []:
        m = re.split(r'\b.\b', result[0])
        if len(m) > 1:
            state = m[1]
    final_State.append(state)

# prepare table title
table_data = [['Name', 'State', 'Physical Address', 'DHCP Enabled'],
              ]
# fill-in the table data
for i in range(len(final_Adapters)):
    table_data.append(
        [final_Adapters[i], final_State[i], final_PHA[i], final_DHCP[i]])
   
# print results
print('\nComputer Information: NIC')
print(tabulate(table_data, headers="firstrow", tablefmt="rounded_outline"))

host_name = (run_command('hostname')[0]).decode('utf-8')
# decode byte stream to utf-8 string format
output = (run_command('systeminfo')[0]).decode('utf-8')
# get rid of 'cursor return' chars
output = re.sub(r'\r', r'', output)
ip = pattern(r'(\[01\]: )(\d+.\d+.\d+.\d+)', 2)[0]
# decode byte stream to utf-8 string format
output = (run_command('ipconfig')[0]).decode('utf-8')
# get rid of 'cursor return' chars
output = re.sub(r'\r', r'', output)
result = re.findall(r'(Gateway.*:) (\d+.\d+.\d+.\d+)', output)
for gw in result:
    if len(gw) > 0:
        gateway = gw[1]
        break
table_data = [[],
              ]
print('Computer Information: IP')
table_data.append(['IPv4 Address', ip])
table_data.append(['GateWay', gateway])
table_data.append(['HostName', host_name])
print(tabulate(table_data, headers="firstrow", tablefmt="rounded_outline"))













