# -*- coding: utf-8 -*-
# sw-4828.py

for t in range(int(input())):
    n = int(input())
    result=list(map(int,input().split()))
    print("#{} {}".format(t+1,max(result)-min(result)))