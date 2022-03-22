import sys
sys.stdin = open('18352_input.txt', 'r')

from collections import deque

def bfs(start, N, K):
    visited = [0] * (N+1)
    visited[start] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if visited[v] == K+1:
            queue.appendleft(v)
            return queue
        for i in cities[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)
    return 0


N, M, K, X = map(int, sys.stdin.readline().rstrip().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
cities = [[] for _ in range(N+1)]
for _ in range(M):
    city1, city2 = map(int, sys.stdin.readline().rstrip().split())
    cities[city1].append(city2)

answer = bfs(X, N, K)
if answer:
    for node in sorted(answer):
        print(node)
else:
    print(-1)

