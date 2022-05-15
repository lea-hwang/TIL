import sys
sys.stdin = open('input.txt', 'r')


def find_root(a):
    first = a
    while parent[a] != a:
        a = parent[a]
    parent[first] = a
    return parent[a]

def union(a, b):
    x = find_root(a)
    y = find_root(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
parent = [i for i in range(V+1)]
graph = []

for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph.append((cost, start, end))

graph.sort()

total = 0
for edge in graph:
    cost, start, end = edge
    if find_root(start) != find_root(end):
        union(start, end)
        total += cost

print(total)

