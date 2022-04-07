import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def BFS(si, sj):
    queue = deque()
    queue.append((si, sj))
    mat[si][sj] = 0
    while queue:
        i, j = queue.popleft()

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and mat[ni][nj]:
                mat[ni][nj] = 0
                queue.append((ni, nj))


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # 세로/가로/배추 수
    mat = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        mat[y][x] = 1

    total = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j]:
                total += 1
                BFS(i, j)

    print(total)