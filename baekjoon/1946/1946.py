import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    people = [0] * (N+1)
    for i in range(N):
        a, b = map(int, input().split())
        people[a] = b
    min_val = 100001
    cnt = 0
    for i in range(1, N+1):
        if min_val > people[i]:
            min_val = people[i]
            cnt += 1
    print(cnt)