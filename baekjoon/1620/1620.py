import sys
sys.stdin = open('1620_input.txt', 'r')

N, M = map(int, input().split())

poketmons = [sys.stdin.readline().rstrip() for _ in range(N)]

for _ in range(M):
    q = sys.stdin.readline().rstrip()
    if q[0] in '0123456789':
        print(poketmons[int(q)-1])
    else:
        print(poketmons.index(q) + 1)