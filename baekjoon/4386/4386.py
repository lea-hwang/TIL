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


n = int(input())
parent = [i for i in range(n+1)]
stars = []
graph = []

for i in range(n):
    stars.append(list(map(float, sys.stdin.readline().split())))

for i in range(n):
    x1, y1 = stars[i]
    for j in range(n):
        if i == j:
            continue
        x2, y2 = stars[j]
        d = ((x1-x2)**2 + (y1-y2)**2) ** (1/2)
        graph.append((d, i+1, j+1))
print(graph)
graph.sort()

total = 0
for edge in graph:
    d, start, end = edge
    if find_root(start) != find_root(end):
        union(start, end)
        total = d
print(total)