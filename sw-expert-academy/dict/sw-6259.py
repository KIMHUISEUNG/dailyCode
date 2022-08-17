# -*- coding: utf-8 -*-
# sw-6259.py

dic_list = {'LETTERS': 0, 'DIGITS': 0}

input_data = input().strip()

for i in input_data:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        dic_list['LETTERS'] += 1
    elif '0' <= i <= '9':
        dic_list['DIGITS'] += 1

print("LETTERS {}".format(dic_list['LETTERS']))
print("DIGITS {}".format(dic_list['DIGITS']))