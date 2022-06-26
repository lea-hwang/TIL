
# 항상 1번 헛간에서 출발
# M개의 양방향 통로가 존재
# 1번 헛간으로부터 가장 거리가 먼 헛간이 가장 안전하다고 판단
# 최단거리: 지나야하는 길의 최소 개수를 의미

import sys
sys.stdin = open('input.txt', 'r')

import heapq

N, M = map(int, input().split())    # 헛간의 개수, 통로의 개수
graph = [[] for _ in range(N + 1)]  # 인접 행렬
INF = int(1e9)
distance = [INF] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면,
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for nxt in graph[now]:
            cost = dist + 1
            if cost < distance[nxt]:
                distance[nxt] = cost # 최단거리 갱신
                heapq.heappush(q, (cost, nxt))

dijkstra(1)

max_nodes = []
max_val = 0
for i in range(1, N+1):
    if max_val < distance[i]:
        max_val = distance[i]
        max_nodes = [i]
    elif max_val == distance[i]:
        max_nodes.append(i)

print(max_nodes[0], distance[max_nodes[0]], len(max_nodes))
