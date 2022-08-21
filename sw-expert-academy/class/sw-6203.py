# -*- coding: utf-8 -*-
# sw-6203.py

class Student:

    def __init__(self,kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    @property
    def total(self):
        return self.__kor + self.__eng + self.__math

    def __repr__(self):
        return "국어, 영어, 수학의 총점: {0}"\
            .format(self.total)


score = input().split(", ")
student = Student(int(score[0]), int(score[1]), int(score[2]))

print(student)