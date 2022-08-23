# -*- coding: utf-8 -*-
# sw-6223.py

class Rectangle:

    def __init__(self,w,h):
        self.__w = w
        self.__h = h

    @property
    def rect_area(self):
        return self.__w * self.__h

    def __repr__(self):
        return "사각형의 면적: {0}".format(self.rect_area)


rectangle = Rectangle(4,5)
print(rectangle)