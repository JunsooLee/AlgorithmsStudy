from sys import stdin

if __name__ == '__main__':
    board = [[0 for _ in range(101)] for _ in range(101)]
    n = int(stdin.readline())
    area = 0

    for _ in range(n):
        x, y = list(map(int, stdin.readline().rstrip().split()))

        for i in range(y, y+10):
            for j in range(x, x+10):
                if board[i][j] == 0:
                    board[i][j] = 1
                    area += 1
    print(area)
