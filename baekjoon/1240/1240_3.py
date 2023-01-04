import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline
N, M = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])
    graph[b].append([a, d])

def find_shortest(cur, end, d):
    global N

    if cur == end:
        return d

    for next, next_d in graph[cur]:
        if not visited[next]:
            visited[next] = True
            dis = find_shortest(next, end, d + next_d)
            if dis != -1:
                return dis
    return -1


for _ in range(M):
    s, e = map(int, input().split())
    visited = [False] * (N+1)
    visited[s] = True
    print(find_shortest(s, e, 0))



