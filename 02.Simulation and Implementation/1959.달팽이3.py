"""
https://loosie.tistory.com/540
간단하고 심플하게 작성한 코드라고 생각한다.
규칙 찾기 문제였지만 규칙 찾기에 약한 모습이 보였다.
다양한 경우의 수를 생각하자.
"""

if __name__ == '__main__':
    M, N = list(map(int, input().split()))

    # 꺾이는 점의 갯수 구하기 (M, N)의 크기에 따라 경우의 수가 다름
    if N < M:
        print(((N - 1) * 2 + 1))
    else:
        print((M - 1) * 2)

    # 끝나는 점의 좌표 찾기
    if M == N:
        if M % 2 == 1:
            print(f'{M//2 + 1} {M//2 + 1}')
        else:
            print(f'{M//2 + 1} {M//2}')
    elif N < M:
        if N % 2 == 0:
            print(f'{N//2 +1} {N//2}')
        else:
            print(f'{N//2 + 1 + (M-N)} {N//2 +1}')
    else:
        if M % 2 == 0:
            print(f'{M//2 + 1} {M//2}')
        else:
            print(f'{M//2 + 1} {M//2 + 1 + (N-M)}')
