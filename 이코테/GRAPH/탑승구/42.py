import sys
sys.stdin = open('input.txt', 'r')

G = int(input())    # 탑승구 수
P = int(input())    # 비행기 수

parent = [i for i in range(G+1)]


# 조상 노드 찾기
def find_root(a):
    first = a
    while parent[a] != a:
        a = parent[a]
    parent[first] = a
    return parent[a]


# gi가 2일 때, 2의 조상노드를 찾고, 해당 조상 노드의 부모노드를 조상노드 -1로 설정.

cnt = 0
for _ in range(P):
    gi = int(sys.stdin.readline().rstrip())
    gi_p = find_root(gi)
    if gi_p == 0:
        break
    else:
        parent[gi_p] = gi_p - 1
        cnt += 1
print(cnt)