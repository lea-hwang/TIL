import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    while P[x] != x:
        x = P[x]
    return x

def union(a, b):
    x = find_set(a)
    y = find_set(b)
    P[y] = x

N, M = map(int, input().split())
P = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

Ps = set()
for i in range(1, N+1):
    Ps.add(find_set(i))
print(len(Ps))