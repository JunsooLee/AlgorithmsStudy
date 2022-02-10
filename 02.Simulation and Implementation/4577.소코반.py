"""
https://westmino.tistory.com/79
해결 방법을 생각하지 못해서 위의 코드를 참고하여 작성하고,
이해하면서 주석을 달아봤다.
문제를 조금더 심플하게 생각해보자...
"""
from sys import stdin


def sokoban(r, c, total, now):
    for o in order:
        if total == now:
            break
        nr = r + direction[o][0]
        nc = c + direction[o][1]

        # Direction을 따라 이동했을 때 해당 위치가 '.'이거나 '+'일 땐 이동
        if arr[nr][nc] in ['.', '+']:
            r, c = nr, nc
        # 해당 위치에 박스가 존재할 경우
        elif arr[nr][nc] in ['b', 'B']:
            # 박스를 이동할 수 있는지 확인하기 위해 바로 앞 한 칸을 확인
            sr = nr + direction[o][0]
            sc = nc + direction[o][1]

            # 박스 앞이 막혀있지 않은 경우
            if arr[sr][sc] in ['.', '+']:
                # 앞이 목적지일 경우 현재 목적지에 들어간 박스의 개수를 증가
                if arr[sr][sc] == '+':
                    now += 1
                # 사람과 박스의 위치를 이동
                arr[nr][nc], arr[sr][sc] = '.', 'b'

                # 만약 사람이 이동한 위치가 목적지였을 경우, 즉 목적지에 있던 상자를 이동시킨 경우엔 현재 상자의 수를 감소
                if (nr, nc) in dest:
                    arr[nr][nc] = '+'
                    now -= 1
                r, c = nr, nc

    arr[r][c] = 'w'
    return now


def print_board(row, col):
    for r in range(row):
        for c in range(col):
            if (r, c) in dest and arr[r][c].isalpha():
                print(arr[r][c].upper(), end='')
            else:
                print(arr[r][c], end='')
        print()


if __name__ == '__main__':
    game = 1
    direction = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    while True:
        row, col = list(map(int, stdin.readline().rstrip().split()))
        if row == 0 and col == 0:
            break

        arr = []  # 게임판 상태를 저장하는 배열
        dest = []  # 박스를 놓을 자리('x')를 저장하는 배열

        start_r, start_c = -1, -1  # 시작점('u' or 'U')의 위치를 저장
        total_box, now_box = 0, 0  # 현재 박스와 전체 박스의 갯수를 저장

        for r in range(row):
            arr.append(list(stdin.readline().rstrip()))
            for c in range(col):
                if arr[r][c] == 'w':  # 만약 w를 만나면 시작점으로 설정해주고 칸을 '.'으로 변경
                    start_r, start_c = r, c
                    arr[r][c] = '.'
                elif arr[r][c] == 'W':  # 만약 W를 만나면 시작점으로 설정하고 해당 지점을 목적지 '+'로 변경
                    start_r, start_c = r, c
                    dest.append((r, c))
                    arr[r][c] = '+'
                elif arr[r][c] == 'b':
                    total_box += 1
                elif arr[r][c] == 'B':
                    total_box += 1
                    now_box += 1
                    dest.append((r, c))
                elif arr[r][c] == '+':
                    dest.append((r, c))

        order = list(stdin.readline().rstrip())
        now_box = sokoban(start_r, start_c, total_box, now_box)

        if now_box == total_box:
            print(f'Game {game}: complete')
        else:
            print(f'Game {game}: incomplete')

        game += 1
        print_board(row, col)
