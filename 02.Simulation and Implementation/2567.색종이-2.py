from sys import stdin


def draw_line():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0

    for i in range(101):
        for j in range(101):
            if arr[i][j] == 1:
                cnt = 0

                for d in range(4):
                    sx, sy = j + dx[d], i + dy[d]
                    if arr[sy][sx] == 1:
                        cnt += 1

                if cnt == 3:
                    result += 1
                elif cnt == 2:
                    result += 2

    return result


arr = [[0 for _ in range(101)] for _ in range(101)]
n = int(stdin.readline())

for _ in range(n):
    x, y = map(int, stdin.readline().rstrip().split())

    for i in range(y, y+10):
        for j in range(x, x+10):
            if arr[i][j] == 0:
                arr[i][j] = 1

print(draw_line())
