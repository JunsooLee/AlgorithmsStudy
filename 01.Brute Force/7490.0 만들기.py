"""
간단한 dfs 문제였다.
Eval 함수를 잘 활용하면 단순히 문자열을 나열하는 것만으로 쉽게 0이되는지 아닌지를 판별할 수 있다.
Eval 함수는 한줄로 정리하자면 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수이다.
마지막에 ASCII 순으로 정렬이 필요하다는 부분을 간과했다.
"""


def dfs(depth, tmp):
    if depth == n:
        expression = ''.join(tmp)

        if eval(expression.replace(' ', '')) == 0:
            result.append(expression)

        return

    for idx in range(3):
        tmp.append(operand[idx] + arr[depth])
        dfs(depth+1, tmp)
        tmp.pop()


if __name__ == '__main__':
    t = int(input())
    operand = ['+', '-', ' ']

    for case in range(t):
        n = int(input())
        arr = [str(i) for i in range(1, n+1)]
        result = []
        dfs(1, ['1'])
        result = sorted(result)

        for r in result:
            print(r)

        print()
