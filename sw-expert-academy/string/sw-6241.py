# -*- coding: utf-8 -*-
# sw-6241.py

# input = http://www.example.com/test?p=1&q=2

url = input()

f_protocol = url.find(':')
f_host = url.rfind('/')
f_others = url.rfind('/')

protocol = url[:f_protocol]
host = url[f_protocol+3:f_host]
others = url[f_others+1:]

print("protocol: {0}".format(protocol))
print("host: {0}".format(host))
print("others: {0}".format(others))