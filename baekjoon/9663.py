import sys
sys.stdin = open('9663_input.txt', 'r')


def check(i):
    for k in range(i):
        if chess[k] == chess[i] or (i - k) == abs(chess[k] - chess[i]):
            return False
    return True

def n_queen(i):
    global cnt, N
    if i == N:
        cnt += 1
        return
    for j in range(N):
        chess[i] = j
        if check(i):
            n_queen(i+1)

N = int(input())
cnt = 0
chess = [0] * N
n_queen(0)

print(cnt)
