import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())

answer = 1
for i in range(m):
    answer *= (n - i)
for i in range(m):
    answer //= (i+1)
print(int(answer))