# -*- coding: utf-8 -*-
# sw-6208.py

class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "이름: {0}".format(self.__name)


class GraduateStudent(Student):

    def __init__(self, name, major):
        self.__name = name
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return "이름: {0}, 전공: {1}".format(self.__name, self.__major)


student = Student('홍길동')
major = GraduateStudent('이순신','컴퓨터')

print(student)
print(major)