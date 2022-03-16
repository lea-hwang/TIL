import sys
from collections import deque
sys.stdin = open('frozen_beverage_input.txt', 'r')

N, M = map(int, input().split())
ice_tray = [list(map(int, input())) for _ in range(N)]

ice_cream = 0
d_rc = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌


def BFS(start):
    queue = deque([start]) # 시작 위치를 큐에 저장한다
    while queue:
        i, j = queue.popleft() # 가장 먼저 들어간 위치를 꺼낸다
        for d_i, d_j in d_rc: # 상 우 하 좌 방향을 살필다
            n_i, n_j = i + d_i, j + d_j
            if 0<=n_i<N and 0<=n_j<M and not ice_tray[n_i][n_j]: # 인덱스를 벗어나지 않으면서, 비어있을 때
                ice_tray[n_i][n_j] = 1
                queue.append((n_i, n_j))


for i in range(N):
    for j in range(M):
        if ice_tray[i][j] == 0:
            BFS((i, j))
            ice_cream += 1


print(ice_cream)


# DFS 재귀로 구현
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def DFS(x, y): # 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    # 주어진 범위를 벗어나는 경우에는 즉시 종료(인덱스)
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if graph[x][y] == 0: # 현재 노드를 아직 방문하지 않았다면
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if DFS(i, j):
            result += 1
print(result)