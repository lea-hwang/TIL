import sys
sys.stdin = open('11651_input.txt', 'r')

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort(key=lambda p:(p[1], p[0]))
for p in xy:
    print(*p)
