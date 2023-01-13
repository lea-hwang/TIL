import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())  # 트리의 정점의 수, 루트의 번호, 쿼리의 수
adjM = [[] for _ in range(N + 1)]  # 간선 정보를 저장할 행렬
children = [[] for _ in range(N + 1)]  # 자식 정보를 저장할 리스트
size = [0] * (N + 1)

for _ in range(N - 1):
    e1, e2 = map(int, input().split())
    adjM[e1].append(e2)
    adjM[e2].append(e1)


def make_tree(current, parent):
    for near in adjM[current]:
        if near != parent:
            children[current].append(near)
            make_tree(near, current)


def count_sub(current):
    size[current] = 1
    for child in children[current]:
        count_sub(child)
        size[current] += size[child]


make_tree(R, -1)
count_sub(R)

for _ in range(Q):  # 각 쿼리에 대한 답 찾기
    root = int(input())
    print(size[root])
