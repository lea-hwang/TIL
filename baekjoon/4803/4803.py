import sys
from collections import deque
sys.stdin = open("input.txt")

# 0 0이 나올 때까지 계속 입력을 받는다.
# 모든 노드를 방문 만약 갔던 곳에 또 방문하게 된다면 그건 그래프
# bfs로 돌면서, 이미 방문했던 곳에 또 방문하면. 그래프.

input = sys.stdin.readline

def bfs(start):
    global n
    # 다음 방문할 곳을 담을 queue
    queue = deque()
    queue.append(start)
    visited[start] = True
    # 방문할 곳이 남아있다면
    while queue:
        # 현재 노드
        cur = queue.pop()
        for next in range(n):
            # 현재 위치에서 넘어갈 다음 노드
            if graph[cur][next]:
                # 이미 방문한 적이 있다면 -> 그래프이기 때문에 return False
                if visited[next]:
                    return False
                # 방문한 적이 없다면, 해당 간선을 지워주고 방문 처리
                graph[cur][next], graph[next][cur] = False, False
                queue.append(next)
                visited[next] = True
    # 그래프가 아니라면 + 1
    return True

case = 0

while True:
    case += 1
    n, m = map(int, input().split())
    # 입력 종료
    if n == m == 0:
        break

    graph = [[False] * (n) for _ in range(n)]

    # 간선 입력
    for i in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1], graph[b-1][a-1] = True, True

    # tree의 개수 헤아리기
    tree_cnt = 0
    visited = [False] * n

    # 모든 노드를 방문하기 위함.
    while sum(visited) < n:
        for i in range(n):
            # 방문한 적이 없다면 해당 노드 방문
            if not visited[i]:
                # 그래프가 아닐 때만 +1
                tree_cnt += bfs(i)
                break

    print(f'Case {case}: ', end='')
    if tree_cnt == 0:
        print('No trees.')
    elif tree_cnt == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {tree_cnt} trees.")


