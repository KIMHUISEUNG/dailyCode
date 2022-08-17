# -*- coding: utf-8 -*-
# sw-6260.py

dic_list = {'UPPER CASE': 0, 'LOWER CASE': 0}

input_data = input().strip()

for i in input_data:
    if 'a' <= i <= 'z':
        dic_list['LOWER CASE'] += 1
    elif 'A' <= i <= 'Z':
        dic_list['UPPER CASE'] += 1

print("UPPER CASE {}".format(dic_list['UPPER CASE']))
print("LOWER CASE {}".format(dic_list['LOWER CASE']))