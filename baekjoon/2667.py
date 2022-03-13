import sys
sys.stdin = open('2667_input.txt')

def BFS(start, N):
    queue = [start]
    apt_map[start[0]][start[1]] = 0 # 처음 위치 이미 방문한 곳으로 바꿈.
    cnt = 1
    d_rc = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상
    while queue:
        i, j = queue.pop()
        #apt_map[row][col] = 0 # 이미 센
        for d in d_rc:
            n_i = i + d[0]
            n_j = j + d[1]
            if 0<=n_i<N and 0<=n_j<N and apt_map[n_i][n_j]:
                apt_map[n_i][n_j] = 0 # 이미 방문한 곳 0으로 바꿈
                queue.append((n_i, n_j))
                cnt += 1
    return cnt


N = int(input())
apt_map = [list(map(int, input())) for _ in range(N)]
apts = []
for i in range(N):
    for j in range(N):
        if apt_map[i][j]:
            apts.append(BFS((i, j), N))

apts.sort()
print(len(apts))
for apt in apts:
    print(apt)
