import sys
from collections import deque

sys.stdin = open("input.txt")

input = sys.stdin.readline
col, row = map(int, input().split())
mat = []
positions = []
for _ in range(row):
    mat.append(list(map(int, input().split())))

for i in range(row):
    for j in range(col):
        if mat[i][j] == 1:
            positions.append((i, j))

def dfs(start):
    queue = deque()
    queue.extend(start)
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    while queue:
        vi, vj = queue.popleft()

        for i in range(4):
            ni, nj = vi + di[i], vj + dj[i]
            if 0 <= ni < row and 0 <= nj < col:
                if mat[ni][nj] == 0:
                    mat[ni][nj] = mat[vi][vj] + 1
                    queue.append((ni, nj))


def check():
    max_days = 0
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                return False
            max_days = max(max_days, mat[i][j])
    return max_days

dfs(positions)

answer = check()

if answer:
    print(answer-1)
else:
    print(-1)
