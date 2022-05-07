# 모든 도시에서 모든 도시까지 -> 플로이드 워셜 알고리즘
import sys
sys.stdin = open('input.txt', 'r')

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]


for _ in range(m):
    start, end, d = map(int, sys.stdin.readline().split())  # 시작 도시, 도착 도시, 도시 간 이동 비용
    if graph[start][end] > d:
        graph[start][end] = d

for i in range(1, n+1): # 시작 도시와 도착 도시가 같을 때 0
    graph[i][i] = 0

for mid in range(1, n+1):     # 중간 도시들의 번호
    for start in range(1, n+1):
        if start == mid:
            continue
        for end in range(1, n+1):
            if end == mid:
                continue
            if graph[start][mid] == INF or graph[mid][end] == INF:
                continue
            elif graph[start][mid] + graph[mid][end] < graph[start][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

