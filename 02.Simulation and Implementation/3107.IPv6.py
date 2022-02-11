from sys import stdin
from typing import List


def func1(ip: List):
    for idx in range(len(ip)):
        if 0 < len(ip[idx]) < 4:
            tmp = '0' * (4-len(ip[idx])) + ip[idx]
            ip[idx] = tmp

    return ip


def func2(ip: List, count: int):
    temp = ['0000' for _ in range(count)]
    index = ip.index('')
    front = ip[:index]
    end = ip[index+1:]

    return front+temp+end


if __name__ == '__main__':
    ipv6 = list(stdin.readline().rstrip().split(':'))
    count = 0

    ip = func1(ipv6)

    if ip[0] == '':
        ip.pop(0)
    elif ip[-1] == '':
        ip.pop()

    for i in ip:
        if len(i) == 4:
            count += 1

    if count != 8:
        ip = func2(ip, 8-count)

    print(':'.join(ip))
