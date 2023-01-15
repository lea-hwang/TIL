import sys
input = sys.stdin.readline

N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingres = [list(map(int, input().split())) for _ in range(N)]

min_cost = int(1e9)
min_ingres = []


def get_min(p, f, s, v, cost, selected, i):
    global min_cost, mp, mf, ms, mv, N, min_ingres
    if cost > min_cost:
        return
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if cost < min_cost:
            min_cost = cost
            min_ingres = [selected]
        else:
            min_ingres.append(selected)
    if i == N:
        return
    vp, vf, vs, vv, vcost = ingres[i]
    get_min(p + vp, f + vf, s + vs, v + vv, cost + vcost, [*selected, i], i + 1)
    get_min(p, f, s, v, cost, selected, i+1)

get_min(0, 0, 0, 0, 0, [], 0)

if len(min_ingres) == 0:
    print(-1)
else:
    print(min_cost)
    for i in sorted(min_ingres)[0]:
        print(i+1, end=" ")
