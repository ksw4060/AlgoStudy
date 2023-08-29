# https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 2023년 8월 29일 화요일

"""
문제 설명
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 20
str은 알파벳으로 이루어진 문자열입니다.
입출력 예
입력 #1

aBcDeFg
출력 #1

AbCdEfG
"""

str = input()
for i in str:
    # i 가 대문자이면, 소문자로 바꿔서 저장
    if i.isupper() == True:
        print(i.lower(), end="")
    # i 가 소문자이면, 대문자로 바꿔서 저장
    else:
        print(i.upper(), end="")


"""
코드를 짜면서 배운 것

isupper(): isupper(), islower() 을 이용하면. 이 문자가 모두 대문자인지 모두 소문자인지 확인하여 Boolean 형태로 나타내 준다.
lower(), upper(): 대문자인지 소문자인지 구분하여 상태를 말해 준다.

파이썬에는 애초에 소문자 > 대문자, 대문자 > 소문자로 바꿔주는 함수가 존재한다.
print(input().swapcase())
"""


"""
다른 풀이
str = input()
print(str.swapcase())
"""
