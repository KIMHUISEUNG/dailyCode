# -*- coding: utf-8 -*-
# sw-6228.py

class Shape:

    @property
    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.__length = length

    @property
    def length(self):
        return self.__length

    @property
    def area(self):
        return self.__length ** 2

    def __repr__(self):
        return "정사각형의 면적: {0}".format(self.area)


square = Square(3)
print(square)
