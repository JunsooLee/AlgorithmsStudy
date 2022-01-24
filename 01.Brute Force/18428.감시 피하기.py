from itertools import combinations
"""
N과 시간제한이 굉장히 넉넉하기 때문에 조합으로 벽을 세울 수 있는 모든 경우를 찾고
각 경우마다 선생님으로부터 학생들이 숨을 수 있는지를 하나하나 확인하는 완전탐색 문제
크기가 작기 때문에 가능한 방법
"""


def can_hide(n, arr, teachers):
    # 각 선생님마다 상,하,좌,우를 확인하여 학생을 만나지 않는지 확인
    for r, c in teachers:
        # 상
        nr, nc = r, c
        while nr > 0:
            nr -= 1
            if arr[nr][nc] == 'S':
                return False
            if arr[nr][nc] == 'O':
                break

        #하
        nr, nc = r, c
        while nr < n-1:
            nr += 1
            if arr[nr][nc] == 'S':
                return False
            if arr[nr][nc] == 'O':
                break

        #좌
        nr, nc = r, c
        while nc > 0:
            nc -= 1
            if arr[nr][nc] == 'S':
                return False
            if arr[nr][nc] == 'O':
                break

        #우
        nr, nc = r, c
        while nc < n-1:
            nc += 1
            if arr[nr][nc] == 'S':
                return False
            if arr[nr][nc] == 'O':
                break

    return True


if __name__ == '__main__':
    n = int(input())
    arr = [input().split(' ') for _ in range(n)]
    empty_list = []
    teacher_list = []
    flag = False

    for row in range(n):
        for col in range(n):
            if arr[row][col] == 'X':
                empty_list.append((row, col))
            elif arr[row][col] == 'T':
                teacher_list.append((row, col))

    for comb in combinations(empty_list, 3):
        # 3개의 벽을 세울 수 있는 조합에 벽을 세움
        for r, c in comb:
            arr[r][c] = 'O'

        if can_hide(n, arr, teacher_list):
            flag = True
            break

        # 숨을 수 없는 경우에는 다시 벽을 원래 상태로 돌림
        for r, c in comb:
            arr[r][c] = 'X'

    print('YES' if flag else 'NO')
