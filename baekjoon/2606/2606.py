import sys
sys.stdin = open('2606_input.txt', 'r')


def DFS(start, N):
    stack = [start]
    while stack:
        now = stack.pop()
        visited[now] = 1
        for i in range(1, N + 1):
            if graph[now][i] and not visited[i]:
                stack.append(i)



N = int(input()) # 정점의 수
M = int(input()) # 간선의 수

graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
visited = [0] * (N + 1)
DFS(1, N)
print(sum(visited) - 1) # 1 제외
