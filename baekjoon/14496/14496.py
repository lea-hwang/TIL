import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

INF = int(1e9)
a, b = map(int, input().split())
N, M = map(int, input().split())

adjM = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
cost = [INF for i in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    adjM[x].append(y)
    adjM[y].append(x)

cost[a] = 0
cost[0] = 0
visited[0] = True

def find_lowest_cost():
    global INF
    min_val = INF
    min_idx = 0
    for i in range(1, N):
        if not visited[i] and min_val > cost[i]:
            min_val = cost[i]
            min_idx = i
    return min_idx

for turn in range(N-1):
    # 방문하지 않은 곳 중에서 제일 비용이 낮은 곳을 pick
    lowest_i = find_lowest_cost()
    # 방문
    visited[lowest_i] = True
    for next_i in adjM[lowest_i]:
        cost[next_i] = min(cost[next_i], cost[lowest_i] + 1)

if cost[b] == INF:
    print(-1)
else:
    print(cost[b])