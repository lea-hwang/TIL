import sys
sys.stdin = open("input.txt")

N = int(input())

value = [0] * (N+1)
for day in range(N):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    value[day] = max(value[day-1], value[day])
    if day + t <= N:
        value[day+t] = max(value[day+t], value[day] + p)

print(max(value[-2], value[-1]))

