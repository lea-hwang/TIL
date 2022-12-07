import sys
from collections import deque
sys.stdin = open("input.txt")

K = int(input())
W, H = map(int, input().split())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(H)]

def in_mat_not_block(i, j):
    global W, H
    return 0<=i<H and 0<=j<W and not mat[i][j]

def bfs(K):
    global W, H
    queue = deque()
    # 시작점
    start = (0, 0)
    queue.append(start)
    visited = [[[0, -1] for j in range(W)] for i in range(H)]
    visited[0][0] = [1, K]

    # 대각선 상상좌, 상좌좌, 좌좌하, 좌하하, 상상우, 상우우, 우우하, 우하하
    ddi = [-2, -1, 1, 2, -2, -1, 1, 2]
    ddj = [-1, -2, -2, -1, 1, 2, 2, 1]
    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    while queue:
        ci, cj = queue.popleft()

        v, k = visited[ci][cj]

        # 도착
        if ci == H-1 and cj == W-1:
            return v
        
        if k > 0:
            for idx in range(8):
                ni, nj = ci + ddi[idx], cj + ddj[idx]
                if in_mat_not_block(ni, nj) and k-1 > visited[ni][nj][1] :
                    visited[ni][nj] = [v + 1, k-1]
                    queue.append((ni, nj))
        
        for idx in range(4):
            ni, nj = ci + di[idx], cj + dj[idx]
            if in_mat_not_block(ni, nj) and k > visited[ni][nj][1]:
                visited[ni][nj] = [v + 1, k]
                queue.append((ni, nj))
    return 0
print(bfs(K) - 1)
