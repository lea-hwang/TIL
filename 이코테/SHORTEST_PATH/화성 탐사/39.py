import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS(N, mat):
    queue = deque()
    INF = 10 * N * N # 최솟값을 찾기 위한 큰 수
    visited = [[INF] * N for _ in range(N)]

    visited[0][0] = mat[0][0]
    queue.append((0, 0))

    while queue:
        ci, cj = queue.popleft() # 현재 위치
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            # 인덱스를 벗어나지 않았을때, 숫자가 더 작을때,
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] > visited[ci][cj] + mat[ni][nj]:
                queue.append((ni, nj)) # 다음 위치 추가
                visited[ni][nj] = visited[ci][cj] + mat[ni][nj]

    return visited[N-1][N-1]


T = int(input())
for _ in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = BFS(N, mat)
    print(result)
