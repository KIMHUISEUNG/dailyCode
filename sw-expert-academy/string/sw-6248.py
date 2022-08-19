# -*- coding: utf-8 -*-
# sw-6248.py

is_number=True
word = input()
result = []

for i in word:
    if i.isdigit() == False:
        result.append(i)

print("".join(result))

