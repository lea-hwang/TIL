import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

s = list(map(int, input().split()))

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 1:
        s[b-1] = c
    elif a == 2:
        s[b-1:c] = [(x+1)%2 for x in s[b-1:c]]
    elif a == 3:
        s[b-1:c] = [0] * (c-b+1)
    else:
        s[b-1:c] = [1] * (c-b+1)

print(*s)