# 로봇은 처음 가로 방향으로 시작

# BFS로 풀기
# 로봇이 갈 수 있는 모든 경로를 탐색하는 걸로.
# 로봇의 현재 위치와, 로봇의 이전 위치, 방향를 저장
# (이전 위치, 현재 위치, 방향) 를 queue에 넣기?
# 이전 위치는 고정, 현재 위치만 이전 위치의 주변으로 바꾸기
#
from collections import deque
board = []
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
N = 0
visited = []

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def next_position(ci, cj, d): # ci, cj: 현재 좌표, d: 0(u), 1(d), 2(l), 3(r) 방향
    nxt = []
    # 현재 방향으로 진행이 가능할 경우 nxt에 추가
    ni, nj = ci + di[d], cj + dj[d]
    if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and not board[ni][nj]: # 인덱스를 벗어나지 않고 가본 적이 없고, 길이 있을 때
        nxt.append((ni, nj, d))     #  다음 위치 저장
        visited[ni][nj] = visited[ci][cj] + 1

    pi, pj = ci - di[d], cj - dj[d]
    # 현재 가로 방향일 때
    if d == 2 or d == 3:
        # 위 두 칸에 모두 길이 있을 때
        if 0<=ci-1<N and not visited[ci-1][cj] and not visited[pi-1][pj] and not board[ci-1][cj] and not board[pi-1][pj]:
            nxt.append((ci-1, cj, 0))
            nxt.append((pi-1, pj, 0))
            visited[ci-1][cj] = visited[ci][cj] + 1
            visited[pi-1][pj] = visited[pi][pj] + 1
        # 아래 두 칸에 모두 길이 있을 때
        if 0<=ci+1<N and not visited[ci+1][cj] and not visited[pi+1][pj] and not board[ci+1][cj] and not board[pi+1][pj]:
            nxt.append((ci+1, cj, 1))
            nxt.append((pi+1, pj, 1))
            visited[ci+1][cj] = visited[ci][cj] + 1
            visited[pi+1][pj] = visited[pi][pj] + 1

    # 현재 새로 방향일 때
    else:
        # 좌 두칸에 모두 길이 있을 때

        # 우 두칸에 모두 길이 있을 때

        # 좌우 확인 후 방향 전환


def solution(board):
    global N, visited, board
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