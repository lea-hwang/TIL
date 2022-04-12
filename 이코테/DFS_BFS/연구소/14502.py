import sys
sys.stdin = open('14502_input.txt', 'r')

from collections import deque

# 0: 빈칸, 1: 벽, 2: 바이러스
N, M = map(int, input().split()) # 세로크기, 가로크기
walls = 0       # 벽의 개수
safe = 0        # 안전한 장소의 개수
matrix = []     # 지도
virus = []      # 바이러스의 위치
empty = []      # 빈 공간의 위치

for _ in range(N):
    matrix.append(list(map(int, input().split())))  # 지도 입력

# 바이러스의 위치 추가
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            virus.append((i, j)) # 바이러스 위치 저장
        elif matrix[i][j] == 1:
            walls += 1  # 벽 개수 저장
        else:
            empty.append((i, j)) # 빈 공간의 위치 저장


def bfs(start):
    global N, M
    queue = deque([start])
    cnt = 1
    while queue:
        i, j = queue.popleft()
        for d_i, d_j in [(1,0),(-1,0),(0,1),(0,-1)]:
            n_i, n_j = i + d_i, j + d_j
            # 인덱스를 벗어나지 않고, 벽이 아니고, 방문하지 않았을때
            if 0<=n_i<N and 0<=n_j<M and (matrix[n_i][n_j] == 0) and not visited[n_i][n_j]:
                visited[n_i][n_j] = 1
                queue.append((n_i, n_j))
                cnt += 1
    return cnt

def build_wall(*ws):
    for w in ws:
        i, j = empty[w][0], empty[w][1]
        matrix[i][j] = 1

def break_wall(*ws):
    for w in ws:
        i, j = empty[w][0], empty[w][1]
        matrix[i][j] = 0

def infection():
    cnt = 0
    for i, j in virus:
        visited[i][j] = 1
        cnt += bfs((i, j))
    return cnt

# 브루트포스
for w1 in range(len(empty)): # 첫번째 놓을 벽
    for w2 in range(w1 + 1, len(empty)): # 두번째 놓을 벽
        for w3 in range(w2 + 1, len(empty)): # 세번째 놓을 벽
            # 벽 세개를 세운다.
            build_wall(w1, w2, w3)

            # bfs로 바이러스를 퍼트린다.
            visited = [[0] * M for _ in range(N)]
            cur_safe = N*M - walls - 3 - infection() # 전체 지도에서 벽 제외, 바이러스 제외
            safe = max(cur_safe, safe)

            # 벽 세개를 허문다
            break_wall(w1, w2, w3)

print(safe)
