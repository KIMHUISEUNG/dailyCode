# -*- coding: utf-8 -*-
# sw-4836-colorinarray.py
# 열 우선 탐색 활용

t = int(input())

for idx in range(t):
    area = [[0] * 10 for _ in range(10)]
    # print(init_list)
    count = 0
    n = int(input())

    for jdx in range(1,n+1):
        row1, col1, row2, col2, color = map(int, input().split())

        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                if color==1:
                    if area[row][col]==0:
                        area[row][col]=1
                    elif area[row][col]==2:
                        area[row][col]=3
                        count+=1
                else:
                    if area[row][col]==0:
                        area[row][col]=2
                    elif area[row][col]==1:
                        area[row][col]=3
                        count+=1
    print("#{} {}".format(idx+1, count))

