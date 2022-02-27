import sys
sys.stdin = open('15649_input.txt', 'r')

def sequence(N, M):
    if M == 0:
        print(*nums)
        return
    for i in range(1, N+1):
        if visited[i]: continue
        visited[i] = 1
        nums.append(i)

        sequence(N, M-1)
        nums.pop()
        visited[i] = 0

# nPr을 구현
N, M = map(int, input().split())
visited = [0] * (N + 1)
nums = []
sequence(N,M)

