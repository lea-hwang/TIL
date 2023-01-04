import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline
N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (N+1) for _ in range(N+1)]

# 현재 위치 -> 현재 위치 이동은 0으로 초기화
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(N-1):
    # 출발지, 도착지, 거리 초기화
    s, e, d = map(int, input().split())
    graph[s][e] = d
    graph[e][s] = d


# 트리이기 때문에 노드 간 통할 수 있는 길은 무조건 하나.
# 이미 방문한 곳 이외의 곳에 갈 때
# bfs 시간초과
from collections import deque

def find_shortest(start, end):
    global N
    visited = [False] * (N + 1)
    visited[start] = True
    queue = deque()
    queue.append([0, start])
    while queue:
        d, v = queue.popleft()

        # 도착
        if v == end:
            return d

        for i in range(1, N+1):
            if not visited[i] and graph[v][i] != INF:
                visited[i] = True
                nd = d + graph[v][i]
                graph[start][i] = nd
                graph[i][start] = nd
                queue.append([nd, i])

for _ in range(M):
    s, e = map(int, input().split())
    print(find_shortest(s, e))



