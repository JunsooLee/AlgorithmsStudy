"""
https://zoosso.tistory.com/155
"""
from sys import stdin

def find_rectangle():
    ans, area = 0, 0

    # 각 줄의 이어진 높이 구하기
    for i in range(1, 100):
        for j in range(100):
            if arr[i][j] == 0:
                continue
            arr[i][j] += arr[i-1][j]

    for _ in range(100, -1, -1):
        print(arr[_])

    for r in range(1, 100):
        for width in range(100):
            height = 100
            for k in range(width, 100):
                # 시작 위치부터 체크해서 가장 낮은 높이 구하기
                height = min(height, arr[r][k])

                if height == 0:
                    break

                area = height * (k - width + 1)
                ans = max(ans, area)

    return ans


if __name__ == '__main__':
    arr = [[0 for _ in range(101)] for _ in range(101)]
    n = int(stdin.readline())

    for _ in range(n):
        x, y = list(map(int, stdin.readline().rstrip().split(' ')))

        for i in range(y, y+10):
            for j in range(x, x+10):
                arr[i][j] = 1

    print(find_rectangle())
