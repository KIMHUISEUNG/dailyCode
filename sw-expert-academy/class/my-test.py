# -*- coding: utf-8 -*-
# my-test.py

class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init__() ...")

    @property
    def family_name(self):
        return self.__family_name


class Child(Parent):
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name)
        # super().__init__(last_name)
        self.__first_name = first_name
        print("Child 클래스의 __init__() ...")

    # @property 를 사용 하면 클래스 내에서 변수 처럼 사용 가능 (getter 방식)
    @property
    def first_name(self):
        return self.__first_name

    # @property명.setter 를 사용 하면 클래스 내에서 변수 처럼 사용 가능 (setter 방식)
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def name(self):
        return "{0} {1}".format(self.family_name, self.first_name)


child = Child("길동", "홍")

print(child.family_name)
print(child.first_name)
print(child.name)
print("========>")
child.first_name = "길순"
print(child.name)