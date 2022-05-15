import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())    # 여행지의 수, 여행 계획에 속한 도시의 수
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 두 여행지의 연결 여부
plan = list(map(int, set(input().split())))
parent = [i for i in range(N+1)]


def find_root(a):
    if parent[a] != a:
        parent[a] = find_root(parent[a])
    return parent[a]

def union(a, b):
    x = find_root(a)
    y = find_root(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in plan:
    for j in plan:
        if graph[i-1][j-1]:
            union(i, j)

# 여행계획의 성공 여부,,,는...음...
# 최소 신장트리를 구해서, 각 여행지 모두 연결되어있는지.
root = parent[plan[0]]
success = True
for city in plan[1:]:
    if parent[city] != root:
        success = False
        break

if success:
    print('YES')
else:
    print('NO')
