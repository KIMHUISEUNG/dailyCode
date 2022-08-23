# -*- coding: utf-8 -*-
# sw-6223.py

class Circle:

    def __init__(self,r):
        self.__r = r

    @property
    def c_area(self):
        return 2*3.14*self.__r

    def __repr__(self):
        return "원의 면적: {0}".format(self.c_area)


circle = Circle(2)
print(circle)