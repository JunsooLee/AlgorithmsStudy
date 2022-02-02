if __name__ == '__main__':
    N, num = int(input()), int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    cur_col, cur_row = 0, 0
    cur_num = N * N
    cur_dir = 0

    for idx in range(cur_num, 0, -1):
        if arr[cur_row][cur_col] == 0:
            arr[cur_row][cur_col] = idx

        if cur_col + move[cur_dir][0] < 0 or cur_col + move[cur_dir][0] >= N or cur_row + move[cur_dir][1] < 0 \
                or cur_row + move[cur_dir][1] >= N or arr[cur_row + move[cur_dir][1]][cur_col + move[cur_dir][0]] != 0:
            cur_dir = (cur_dir + 1) % 4

        cur_col = cur_col + move[cur_dir][0]
        cur_row = cur_row + move[cur_dir][1]

    for row in range(N):
        for col in range(N):
            if arr[row][col] == num:
                rfind = row+1
                cfind = col+1

            print(arr[row][col], end=' ')
        print()

    print(rfind, cfind)

