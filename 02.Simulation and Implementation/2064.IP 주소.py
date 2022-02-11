"""
https://txegg.tistory.com/112
"""
from sys import stdin

if __name__ == '__main__':
    n = int(stdin.readline())
    ip = [stdin.readline().rstrip().split('.') for _ in range(n)]

    mask, address = [], []

    # 4자리의 IP 주소에서 각각의 주소의 idx(0~3)번째를 비교하며 값을 추가
    for idx in range(4):
        min_ip = int(ip[0][idx])  # N개의 주소들의 idx번째 자리의 최소값
        max_ip = int(ip[0][idx])  # N개의 주소들의 idx번째 자리의 최대값

        for tmp_ip in ip:
            if max_ip < int(tmp_ip[idx]):
                max_ip = int(tmp_ip[idx])
            if min_ip > int(tmp_ip[idx]):
                min_ip = int(tmp_ip[idx])

        # ~255(11111111) = -256(-100000000)
        # max ip == min ip인 경우, ex) 194(11000010)일 때, ~194 = -195(-11000011)
        """
        네트워크 마스크는 XOR연산과 NOT연산을 같이해서 NXOR 연산으로 값을 구한 다음,
        256을 더하면 네트워크 마스크가 나옵니다.
        """
        if 255 == 256 + (~max_ip ^ min_ip):
            mask.append(255)
        else:
            for j in range(9):
                if -(~max_ip ^ min_ip) <= 1 << j:
                    mask.append(256 - (1 << j))

                    for k in range(3):
                        mask.append(0)
                    break
        address.append(int(ip[0][idx]) & mask[idx])

    mask = mask[:4]

    print(f'{address[0]}.{address[1]}.{address[2]}.{address[3]}')
    print(f'{mask[0]}.{mask[1]}.{mask[2]}.{mask[3]}')

