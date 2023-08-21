# 파이썬 장고 실무 심화 5주차 11강. classMethod에 대한 코드.
# 작성일/인 : 2023년 8월 21일 (월). 김성우
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear (cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()
# 인스턴스를 만들고 나서, display 함수를 실행시키고 있다.
person1 = Person.fromBirthYear('김성우', 1992)
person1. display()
# 인스턴스가 존재하지 않은데도, 클레스메소드로 바로 실행해줬다.
