import sys
sys.stdin = open("input.txt")

N, M, R = map(int, sys.stdin.readline().rstrip().split())
mat = [[] for i in range(N)]

for i in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    mat[start-1].append(end-1)
    mat[end-1].append(start-1)

for i in range(N):
    mat[i].sort(key=lambda x: -x)

visited = [0] * N
def dfs(x):
    global N
    stack = []
    stack.append(x)
    time = 0
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        time += 1
        visited[v] = time
        for i in mat[v]:
            if not visited[i]:
                stack.append(i)


dfs(R-1)

for i in range(N):
    print(visited[i])
