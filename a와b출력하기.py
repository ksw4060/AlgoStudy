# https://school.programmers.co.kr/learn/courses/30/lessons/181951
# 2023년 8월 29일 화요일


"""
문제 설명
정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

제한사항
-100,000 ≤ a, b ≤ 100,000

입출력 예
입력 #1
4 5
"""

a, b = map(int, input().strip().split(' '))
if a > -999999 and b < 999999:
    print ("a = "+str(a))
    print ("b = "+str(b))
else:
    print("잘못된 입력입니다")
