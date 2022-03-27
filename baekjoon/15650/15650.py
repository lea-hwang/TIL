import sys
sys.stdin = open('15650_input.txt', 'r')

def combination(N, M, p):
    if M == 0:
        print(*nums)
        return

    for i in range(p, N+1):
        if visited[i]: continue

        visited[i] = 1
        nums.append(i)
        combination(N, M-1, i)
        visited[i] = 0
        nums.pop()


N, M = map(int, input().split())
visited = [0]*(N+1)
nums = []
combination(N, M, 1)
