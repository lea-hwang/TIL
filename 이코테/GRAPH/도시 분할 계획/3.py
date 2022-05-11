import sys

# 루트 노드 찾기
def find_root(parent, a):
    if parent[a] != a:
        parent[a] = find_root(parent, parent[a])
    return parent[a]


# 두 집합 합치기
def union(parent, a, b):
    x = find_root(parent, a)
    y = find_root(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 입력
N, M = map(int, input().split()) # 집의 개수, 길의 수
graph = []  # 간선 정보 저장
parent = [i for i in range(N+1)]
total_cost = 0
last = 0

# 길정보 입력 받기
for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())     # A -> B 비용: C
    graph.append((C, A, B))

# 비용을 기준으로 오름차순 정렬
graph.sort(key=lambda x: x[0])

# 작은 비용을 가진 노드를 계속해서 선택하기, 대신 사이클 생성 X
for cost, start, end in graph:
    # 사이클이 발생하지 않을때 -> a, b의 find_root 값이 서로 다를 때
    if find_root(parent, start) != find_root(parent, end):
        union(parent, start, end)
        total_cost += cost
        last = cost


print(total_cost - last)