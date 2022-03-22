import sys
sys.stdin = open('maze_escape_input.txt', 'r')


def BFS(start):
    visited[0][0] = 1
    queue = [start]
    d_rc = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
    while queue:
        i, j = queue.pop()
        for d in d_rc:
            n_i = i + d[0]
            n_j = j + d[1]
            # 인덱스를 벗어나지않고, 괴물이 없고, 방문한 적이 없으면
            if 0<=n_i<N and 0<=n_j<M and maze[n_i][n_j] and not visited[n_i][n_j]:
                visited[n_i][n_j] = visited[i][j] + 1
                queue.append((n_i, n_j))


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
BFS((0, 0))
if visited[N-1][M-1]:
    print(visited[N-1][M-1])
else:
    print(0)