import sys
sys.stdin = open("input.txt")

from collections import deque

a, b = map(int, input().split())
MAX = 100001
counts = [-1] * MAX
visited = [False] * MAX

def find_b(a, b):

    queue = deque()
    queue.append(a)
    visited[a] = True
    counts[a] = 0

    while queue:
        v = queue.popleft()
        if v == b:
            return
        
        if 2*v < MAX and not visited[2*v]:
            counts[2*v] = counts[v]
            queue.appendleft(2*v) # 우선순위를 위함
            visited[2*v] = True
        
        if 0 <= v-1 and not visited[v-1]:
            counts[v-1] = counts[v] + 1
            queue.append(v-1)
            visited[v-1] = True
        
        if v+1 < MAX and not visited[v+1]:
            counts[v+1] = counts[v] + 1
            queue.append(v+1)
            visited[v+1] = True
        
    
find_b(a, b)
print(counts[b])