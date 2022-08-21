# -*- coding: utf-8 -*-
# 15-15.py

class Student:

    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    # property 선언은 읽기 전용
    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    # property 에 setter 선언 까지 하면 읽기에 쓰기 전용
    @height.setter
    def height(self, height):
        self.__height = height

    # 대부분의 객체를 출력 할 때에 많이 사용하는 함수
    # 객체의 표현을 지원해 주는 '리프리젠테이션' __repr__ 사용
    def __repr__(self):
        return "{0}(name: {1}, gender: {2}, height: {3})"\
            .format(self.__class__.__name__, self.name, self.gender, self.height)


students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.4),
    Student("강감찬", "남", 182.2)
]

for student in students:
    print(student)

# sorted 함수는 반복가능한 객체 대상 사용자 정의
# 객체 사용 시 해당 리스트 객체에 있는 각 항목에서 키를 사용한 정보 전달
# sorted(반복 가능 객체, key=(기준이 되는 key 값), reverse=False(기본값))

print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name):
    print(student)

print("name으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=True):
    print(student)

print("height로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height):
    print(student)

print("height로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height, reverse=True):
    print(student)