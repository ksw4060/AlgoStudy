# https://www.acmicpc.net/problem/18870 좌표압축
# https://velog.io/@zinu/%EB%B0%B1%EC%A4%80-18870-%EC%A2%8C%ED%91%9C-%EC%95%95%EC%B6%95%ED%8C%8C%EC%9D%B4%EC%8D%AC 참고 블로그

"""
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
"""

import sys

n = int(sys.stdin.readline())
numbers_list = list(map(int, sys.stdin.readline().split()))
sorted_array_list = sorted(set(numbers_list))

dic = {sorted_array_list[i]:i for i in range(len(sorted_array_list))}
for i in numbers_list:
    print(dic[i], end=" ")
