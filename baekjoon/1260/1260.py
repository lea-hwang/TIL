import sys
sys.stdin = open('1260_input.txt', 'r')

def DFS(start):
    visited = [0] * (N+1)
    stack = [start] # 처음 위치 stack에 넣어주기
    order = []
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = 1
            order.append(now)
        for next in range(N, 0, -1):
            if graph[now][next] and not visited[next]:
                stack.append(next)
    return order

def BFS(start):
    visited = [0] * (N+1)
    queue = [start]
    order = [start]
    visited[start] = 1
    while queue:
        now = queue.pop(0)
        for next in range(N+1):
            if graph[now][next] and not visited[next]:
                queue.append(next)
                visited[next] = 1
                order.append(next)
    return order

N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작 정점의 번호
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # 그래프 만들기
    graph[a][b] = graph[b][a] = 1

print(*DFS(V))
print(*BFS(V))


