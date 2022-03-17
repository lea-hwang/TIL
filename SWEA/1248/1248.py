import sys
sys.stdin = open('1248_input.txt', 'r')


def ancestor(cur):
    anc = []
    while parent[cur]:
        anc.append(parent[cur])
        cur = parent[cur]
    return anc


def find_coancestor(A, B):
    A_anc = ancestor(A)
    B_anc = ancestor(B)
    for k in A_anc:
        if k in B_anc:
            return k


def count_nodes(cur):
    global cnt, V
    if cur and cur <= V:
        cnt += 1
        count_nodes(children[cur][0])
        count_nodes(children[cur][1])



T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    edges = list(map(int, input().split()))
    parent = [0] * (V+1)
    children = [[0] * 2 for _ in range(V+1)]
    for i in range(E):
        p, c = edges[2*i], edges[2*i+1]
        parent[c] = p
        if not children[p][0]:
            children[p][0] = c
        else:
            children[p][1] = c

    co_anc = find_coancestor(A, B)
    cnt = 0
    count_nodes(co_anc)
    print(f'#{tc} {co_anc} {cnt}')