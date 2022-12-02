import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

mat = [[0] * (N + 1)]
for i in range(N):
    mat.append([0] + list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        mat[i][j] = mat[i-1][j] + mat[i][j-1] + mat[i][j] - mat[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    print(mat[x2][y2] - mat[x2][y1-1] - mat[x1-1][y2] + mat[x1-1][y1-1])