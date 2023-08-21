# 파이썬 장고 실무 심화 5주차 12강. staticMethod에 대한 코드.
# 작성일/인 : 2023년 8월 21일 (월). 김성우
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year )

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age): # self 가 들어가지 않는 것이 특이점.
        return age > 18

    def display(self):
        print(self.name + "의 나이 : " + str(self.age) + "입니다")


person1 = Person('사람1', 21) # 인스턴스 생성 후
person1.display()

person2 = Person.fromBirthYear('사람2', 1992) # 인스턴스 생성하지 않고, 클래스메서드로
person2.display()

print(person1.isAdult(22))
print(person1.isAdult(15))
print(person1.isAdult(32))
