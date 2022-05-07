# 1번 회사 출발 -> K번 회사 방문 -> X번 회사 방문

# 플로이드 워셜
# 1. 초기 설정
#   1) graph : 각 방향의 최단거리를 저장할 매트릭스 생성 (초기값은 무한대)
#
# 2. 알고리즘
#   1) 포문을 통해 각각의 노드 번호(i)가 중간 지점이 될 수 있도록 한다음.
#   2) 현재 최단거리와 비교하여 i번째 노드를 거쳐갈 때 더 거리가 짧은 경우 갱신

import sys
sys.stdin = open('input.txt', 'r')

# 1. 노드끼리의 최단거리를 저장할 매트릭스 생성(초기값은 무한대)
N, M = map(int, input().split())                # 전체 회사의 개수, 경로의 개수
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]      # 초기값 무한대

# 2. 간선 정보를 이용하여 노드끼리의 최단거리 1로 갱신(양방향)
for _ in range(M):
    start, end = map(int, input().split())      # 노드끼리의 거리는 1. 양방향
    graph[start][end] = 1
    graph[end][start] = 1

X, K = map(int, input().split())

# 3. 플로이드 워셜로 접근 -> 모든 방향에서 모든 방향으로 가는 것이기 때문
# mid를 중간지점으로 거쳐가는 거리의 합이 현재 최단거리보다 짧을 경우 갱신
for mid in range(1, N+1):               # mid : 중간에 거쳐갈 노드 번호
    for start in range(1, N+1):
        if mid == start:                # 시작이 중간지점이 아닐 때 제외
            continue
        for end in range(1, N+1):
            if mid == end:              # 끝이 중간지점이 아닐 때 제외
                continue
            if start == end:            # 시작과 끝이 같을 때 0
                graph[start][end] = 0
                graph[end][start] = 0
            elif graph[start][mid] == INF or graph[mid][end] == INF: # 거쳐가는 길이 무한대일 때
                continue
            elif graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

# 1번에서 시작해서 K를 거쳐 X 방문
total = 0
if graph[1][K] == INF or graph[K][X] == INF:
    print(-1)
else:
    print(graph[1][K] + graph[K][X])

