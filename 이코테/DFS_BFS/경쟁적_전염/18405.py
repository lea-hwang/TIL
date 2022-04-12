import sys
sys.stdin = open('18405_input.txt', 'r')

from collections import deque

def bfs(start): # start = [(0,0), (0,2), (2,0)]
    global N, S
    queue = deque(start)
    visited = [[0] * N for _ in range(N)]
    for i, j in start:
        visited[i][j] = 1
    while queue:
        i, j = queue.popleft()
        if visited[i][j] == S+1:
            return
        for d_i, d_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n_i, n_j = i + d_i, j + d_j
            if 0<=n_i<N and 0<=n_j<N and not matrix[n_i][n_j] and not visited[n_i][n_j]:
                visited[n_i][n_j] = visited[i][j] + 1
                matrix[n_i][n_j] = matrix[i][j]
                queue.append((n_i, n_j))

N, K = map(int, input().split()) # 시험관 크기, 바이러스 개수
matrix = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus = [[] for _ in range(K+1)]

# 바이러스 위치 찾기
for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            virus[matrix[i][j]].append((i, j))

for i in range(K):
    virus[i].sort()
virus = sum(virus, [])

# 바이러스 전염시키기
bfs(virus)

print(matrix[X-1][Y-1])

