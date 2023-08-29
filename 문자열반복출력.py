# https://school.programmers.co.kr/learn/courses/30/lessons/181950
# 2023년 8월 29일 화요일

"""
문제 설명
문자열 str과 정수 n이 주어집니다.
str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 10
1 ≤ n ≤ 5

입력 #1

string 5
"""
a, b = input().strip().split(' ')
b = int(b)
print(a*b)
