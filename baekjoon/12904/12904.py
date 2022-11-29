# 유형: 그리디
# 풀이방법:
# T -> S 로 돌아가는 방법을 생각.

import sys
sys.stdin = open('input.txt', 'r')

S = input()
T = input()

s_len = len(S)
t_len = len(T)

while s_len < t_len:
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1][::-1]
    t_len -= 1

if S == T:
    print(1)
else:
    print(0)
