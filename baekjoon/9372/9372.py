import sys
sys.stdin = open('9372_input.txt', 'r')


def find_root(a):
    first = a
    while a != parent[a]:
        a = parent[a]
    parent[first] = a
    return parent[a]


def union(a, b):
    x = find_root(a)
    y = find_root(b)
    if x < y :
        parent[y] = x
    else:
        parent[x] = y


T = int(input())

for test in range(T):
    N, M = map(int, input().split())     # 국가의 수, 비행기 종류
    parent = [i for i in range(N + 1)]

    cnt = 0
    # 비행기 정보
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        if find_root(start) != find_root(end):
            union(start, end)
            cnt += 1

    print(cnt)


    print(parent)