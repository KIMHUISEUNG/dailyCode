# -*- coding: utf-8 -*-
# sw-4835.py

for t in range(int(input())):
    n, m = map(int,input().split())
    number = list(map(int,input().split()))
    new=[]
    for i in range(n-m+1):
        result=0
        for j in range(i,i+m):
            result+=number[j]
        new.append(result)
    print("#{0} {1}".format(t+1,max(new)-min(new)))