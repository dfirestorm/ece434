#!/usr/bin/env python3
top_dir = '/sys/class/hwmon/'
f1 = open(f'{top_dir}hwmon0/temp1_input','r')
f2 = open(f'{top_dir}hwmon1/temp1_input','r')
f3 = open(f'{top_dir}hwmon2/temp1_input','r')
listf = [f1,f2,f3]
values = []
for f in listf:
    values.append(f.read().splitlines()[0])
    f.seek(0)
print(values)