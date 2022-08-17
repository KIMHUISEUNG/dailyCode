# -*- coding: utf-8 -*-
# sw-6262.py

input_data = input()
result = {}

for i in input_data:
    count = result.get(i,0)
    result[i] = count + 1

for j, k in result.items():
    print("{0},{1}".format(j,k))
