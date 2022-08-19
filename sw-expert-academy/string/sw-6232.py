# -*- coding: utf-8 -*-
# sw-6232.py

word = input()

is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 -i]:
        is_palindrome = False
        break

if is_palindrome == True:
    print(word)
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print(word)
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")