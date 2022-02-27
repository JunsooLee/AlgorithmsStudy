"""
처음에는 단순 Brute Force로 문제를 풀었지만 제약 조건의 값이 커서 시간 초과가 발생했다.
프로그래머스에서 비슷한 문제를 이분탐색으로 풀었던 기억이 생각나서 풀었다.
문제를 잘 읽고 푸는 것이 중요하다.
"""
from sys import stdin

k, n = map(int, stdin.readline().rstrip().split(' '))
cable = [int(stdin.readline()) for _ in range(k)]
answer = 0

left, right = 1, max(cable)

while left <= right:
    count = 0
    mid = (left + right) // 2

    for c in cable:
        count += (c // mid)

    if n <= count:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)