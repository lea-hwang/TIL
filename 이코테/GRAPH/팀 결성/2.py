import sys
sys.stdin = open('input.txt', 'r')


# 합치기
def union(parent, a, b):
    x = find_root(parent, a)
    y = find_root(parent, b)
    # 둘 중 더 작은 수가 부모 노드
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# root 찾기
def find_root(parent, a):
    if parent[a] != a:
        parent[a] = find_root(parent, parent[a])
    return parent[a]


# 입력
N, M = map(int, input().split()) # N: 학생번호(0~N), M: 연산 수

# parent 자기 자신으로 초기화
parent = [i for i in range(0, N+1)]

# 연산
for i in range(M):
    op, a, b = map(int, input().split())
    # 팀 합치기
    if op == 0:
        union(parent, a, b)

    # 같은 팀 여부 확인
    else:
        if find_root(parent, a) == find_root(parent, b):
            print('YES')
        else:
            print('NO')








