import sys
sys.stdin = open('5525_input.txt', 'r')

N = int(input()) # P에서 OI의 반복 횟수
M = int(input()) # S의 길이
S = input()

cnt = 0
i = 0
while i < M:
    if S[i] == 'I':
        k = 0 # I 뒤의 OI의 반복횟수
        while True:
            ni = i + 1 + 2*k
            if S[ni:ni+2] == 'OI':
                k += 1
            else:
                break
        if k and k >= N:
            cnt += (k-N) + 1
        i += 2 * k + 1
    else:
        i += 1
print(cnt)