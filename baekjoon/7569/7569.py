import sys
from collections import deque

input = sys.stdin.readline
col, row, height = map(int, input().split())

mat = [[[] for _ in range(row)] for _ in range(height)]

for h in range(height):
    for i in range(row):
        mat[h][i] = list(map(int, input().split()))

position = []
for h in range(height):
    for i in range(row):
        for j in range(col):
            if mat[h][i][j] == 1:
                position.append((h, i, j))

def dfs(vs):
    queue = deque()
    di = [0, 0, -1, 1, 0, 0]
    dj = [-1, 1, 0, 0, 0, 0]
    dk = [0, 0, 0, 0, -1, 1]
    queue.extend(vs)

    while queue:
        vk, vi, vj  = queue.popleft()
        for i in range(6):
            nk, ni, nj  = vk + dk[i], vi + di[i], vj +dj[i]
            # 인덱스를 벗어나지 않고, 토마토가 익지 않았을 때, 방문
            if 0<=ni<row and 0<=nj<col and 0<=nk<height:
                if mat[nk][ni][nj] == 0:
                    mat[nk][ni][nj] = mat[vk][vi][vj] + 1
                    queue.append((nk, ni, nj))


dfs(position)

def check():
    max_days = 0
    for h in range(height):
        for i in range(row):
            for j in range(col):
                if mat[h][i][j] == 0:
                    return False
                max_days = max(max_days, mat[h][i][j])
    return max_days               

answer = check()
print(answer-1 if answer else -1)
