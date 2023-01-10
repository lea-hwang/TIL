import sys
import heapq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
children = [[] for _ in range(N+1)]
max_d = [[0] for _ in range(N+1)]
for i in range(N-1):
    p, c, d = map(int, input().split()) # 부모, 자식, 거리
    children[p].append((c, d))

# 후위순회
def postorder(v):
    for child in children[v]:
        c, d = child
        postorder(c)
        max_d[v].append(d + max(max_d[c]))

postorder(1)

answer = 0
for i in range(1, N+1):
    answer = max(answer, sum(heapq.nlargest(2, max_d[i])))
print(answer)
