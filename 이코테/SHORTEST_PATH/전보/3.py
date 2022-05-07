# 문제 분석
# 단방향 그래프, 한 도시에서 다른 모든 도시까지 최단거리 -> 다익스트라

# 메세지를 받은 도시의 수와 전체 시간?

# 다익스트라
# 1. 초기값 설정
#   1) distance: 각각의 노드까지의 최단거리를 저장할 리스트 생성(초기값 무한대)
#   2) graph: 인접 노드사이의 거리를 저장할 행렬
#   3) visited: 노드 방문 여부 저장
#   4) heap: 노드 사이의 간선정보가 저장된 최소 힙

# 2. 알고리즘
#   1) 현재 노드를 기준으로 인접 노드까지의 거리를 heap에 저장
#   2) 힙에 담겨있는 노드들을 기준으로 방문한 적이 없고, 거리가 제일 짧은 인접 노드를 pop하여 방문 및 현재 노드로 지정

import heapq
import sys
sys.stdin = open('input.txt', 'r')

N, M, C = map(int, input().split())         # 도시의 개수, 통로의 개수, 메세지를 보내고자 하는 도시
INF = int(1e9)
distance = [INF] * (N+1)                    # 도시 간 최단거리 저장할 리스트
graph = [[] * (N+1) for _ in range(N+1)]    # 도시 간 거리가 저장될 행렬
visited = [False] * (N+1)                   # 도시 방문 여부
heap = []                                   # 인접 노드와 그 사이 거리를 오름차순으로 저장할 힙

# 인접 행렬 정리
for _ in range(M):
    start, end, d = map(int, input().split())
    graph[start].append((end, d))

heapq.heappush(heap, (C, 0))                # 시작 도시와 그 거리(0) 추가

while heap:
    V, d = heapq.heappop(heap)                  # 현재 방문하려는 도시와 거리
    if not visited[V]:                          # 방문한 적이 없다면
        visited[V] = True                       # 도시 방문
        distance[V] = d                         # 최단 거리 갱신
        for nV, nd in graph[V]:                 # 다음에 방문할 도시 선정
            heapq.heappush(heap, (nV, d+nd))

total_city = 0                                  # 방문한 도시 수
max_distance = 0                                # 전체 도시 간 거리 합
for i in range(1, N+1):
    if distance[i] == INF:                      # 방문한 적이 없을 때
        continue
    if i == C:                                  # 시작 도시일 때
        continue
    total_city += 1
    max_distance = max(max_distance, distance[i])

print(distance)
print(total_city, max_distance)