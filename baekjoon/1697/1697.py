import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

ops = {
    0:lambda x: x-1,
    1:lambda x: x+1,
    2:lambda x: x*2,
}

def BFS(start, end):
    queue = deque()
    queue.append(start)
    visited = [0] * 100001
    visited[start] = 1
    while queue:
        v = queue.popleft()
        if v == end:
            return visited[v] - 1
        for i in range(3):
            nv = ops[i](v)
            if 0<=nv<=100000 and not visited[nv]:
                visited[nv] = visited[v] + 1
                queue.append(nv)

N, K = map(int, input().split())

print(BFS(N, K))
