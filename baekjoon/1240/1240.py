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


# 플로이드 워셜
# s -> e 보다 s -> m -> e가 더 빠른 경우 갱신
# 시간초과
for s in range(1, N+1):
    for e in range(1, N+1):
        for m in range(1, N+1):
            graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])
            graph[e][s] = graph[s][e]


for _ in range(M):
    s, e = map(int, input().split())
    print(graph[s][e])



