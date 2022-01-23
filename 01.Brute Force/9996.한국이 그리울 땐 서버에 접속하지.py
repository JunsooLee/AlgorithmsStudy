"""N = int(input())
pattern = list(input())
asterisk = pattern.index('*')

for idx in range(N):
    file = input()
    flag = True

    if len(file) <= 2:
        if file[0] != pattern[0] or file[-1] != pattern[-1]:
            flag = False
    else:
        temp = ['*' for _ in range(len(file))]
        temp[:asterisk] = pattern[:asterisk]
        start = len(pattern) - asterisk
        temp[len(temp)-start+1:len(temp)] = pattern[start:len(pattern)]

        for j in range(len(file)):
            if temp[j] != file[j] and temp[j] != '*':
                flag = False
                break

    print('DA' if flag else 'NE')"""

import re

N = int(input())
front, back = input().split('*')
# front 문자열 뒤에 '*'가 있고 back 문자열이 1개 이상
pattern = re.compile(front+'.'+'*'+back+'+')

for idx in range(N):
    file = input()
    result = pattern.search(file)

    # Match 객체가 존재하고 Match되는 문자열이 파일 이름과 같다면 'DA' 그 외에는 'NE'
    print('DA' if result and result.group() == file else 'NE')
