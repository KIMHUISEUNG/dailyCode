# -*- coding: utf-8 -*-
# sw-4834.py

# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력
# 카드 장수가 같을 때는 적힌 숫자가 큰쪽을 출력

for t in range(int(input())):
    n = int(input())
    number = list(map(int,input()))

    card = [0] * 10
    # card  [0,0,0,0,0,0,0,0,0,0]

    for i in range(n):
        card[int(number[i])] += 1
    result=0

    for i in range(len(card)):
        if result <= card[i]:
            result = card[i]
            idx = i

    print("#{0} {1} {2}".format(t+1, idx, result))



