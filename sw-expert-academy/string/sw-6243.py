# -*- coding: utf-8 -*-
# sw-6243.py

word = '산 하늘 강 바다 하늘 강 들'

data = list(set(word.split(' ')))
result = sorted(data)
print(",".join(result))