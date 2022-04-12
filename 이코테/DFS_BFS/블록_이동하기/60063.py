# 로봇은 처음 가로 방향으로 시작

# 만약 DFS로 푼다면
# 로봇이 할 수 있는 행동...?
# 상하좌우로 이동 or 회전

#(0,1)을 기준으로 최단거리



from collections import deque
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def solution(board):
    answer = 0
    N = len(board)
    si, sj = 0, 1 # 시작점

    queue = deque()
    queue.append((si, sj))
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1

    while queue:
        i, j = queue.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            # 인덱스를 벗어나지 않고, 방문한 적이 없을 때
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                visited[ni][nj]


    return answer



solution(board)