"""
혼자서 풀기엔 어려웠다...
DFS를 활용해서 예제 문제는 풀었지만 체점 과정에서 반례가 있었다...
밑의 블로그를 참고하여 코드를 수정해봤다.
https://chelseashin.tistory.com/96
"""


def check(num):
    global available
    r = num // 5
    c = num % 5

    for d in move:
        nr = r + d[0]
        nc = c + d[1]
        if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc]:
            continue

        next_num = nr * 5 + nc
        if next_num in p:
            visited[nr][nc] = 1
            available += 1
            check(next_num)


def dfs(depth, y_cnt, idx):
    global result, available, visited

    if y_cnt > 3 or 25-idx < 7 - depth:  # 조건 불만족시 미리 Return
        return

    if depth == 7:
        available = 1
        visited = [[0] * 5 for _ in range(5)]

        sr, sc = p[0] // 5, p[0] % 5
        visited[sr][sc] = 1

        check(p[0])

        if available == 7:
            result += 1
        return

    r = idx // 5
    c = idx % 5

    if arr[r][c] == 'Y':
        p.append(idx)
        dfs(depth+1, y_cnt+1, idx+1)
        p.pop()
    else:
        p.append(idx)
        dfs(depth+1, y_cnt, idx+1)
        p.pop()

    dfs(depth, y_cnt, idx+1)


if __name__ == '__main__':
    arr = [list(input()) for _ in range(5)]
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = 0
    p = []

    dfs(0, 0, 0)  # (depth, Y의 갯수, 사용할 숫자 인덱스)

    print(result)
