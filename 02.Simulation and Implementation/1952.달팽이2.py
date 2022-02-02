if __name__ == '__main__':
    M, N = list(map(int, input().split()))
    arr = [[0 for _ in range(N)] for _ in range(M)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    cur_row, cur_col = 0, 0
    cur_dir = 0
    turn = 0

    for idx in range(M*N):
        if arr[cur_row][cur_col] == 0:
            arr[cur_row][cur_col] = idx + 1

        if cur_row + move[cur_dir][0] < 0 or M <= cur_row + move[cur_dir][0] \
                or cur_col + move[cur_dir][1] < 0 or N <= cur_col + move[cur_dir][1] \
                or arr[cur_row + move[cur_dir][0]][cur_col + move[cur_dir][1]] != 0:
            cur_dir = (cur_dir + 1) % 4
            turn += 1

        cur_row += move[cur_dir][0]
        cur_col += move[cur_dir][1]

    print(turn - 1)