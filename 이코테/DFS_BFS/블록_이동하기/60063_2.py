import sys
sys.stdin = open('input.txt', 'r')


def next_position(ci, cj, d):
    global visited, board, di, dj, N
    nxt = []
    # 현재 방향으로 진행이 가능할 경우 nxt에 추가
    ni, nj = ci + di[d], cj + dj[d]
    if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and not board[ni][nj]:  # 인덱스를 벗어나지 않고 가본 적이 없거나 횟수가 동일할 때, 길이 있을 때
        nxt.append((ni, nj, d))                     # 다음 위치 저장
        visited[ni][nj] = 1                         # 방문

    ni, nj = ci - 2 * di[d], cj - 2 * dj[d]
    if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and not board[ni][nj]:  # 인덱스를 벗어나지 않고 가본 적이 없거나 횟수가 동일할 때, 길이 있을 때
        nxt.append((ni, nj, (d//2)*2 + (d+1)%2))    # 다음 위치 저장
        visited[ni][nj] = 1                         # 방문

    pi, pj = ci - di[d], cj - dj[d]
    # 현재 가로 방향일 때
    if d == 2 or d == 3:
        # 위 두 칸에 모두 길이 있을 때
        if 0<=ci-1<N and not board[ci-1][cj] and not board[pi-1][pj]:
            if not visited[ci-1][cj] and not visited[pi-1][pj]:
                nxt.append((ci-1, cj, d))
            if not visited[ci-1][cj]:
                nxt.append((ci-1, cj, 0))
                visited[ci-1][cj] = 1
            if not visited[pi-1][pj]:
                nxt.append((pi-1, pj, 0))
                visited[pi-1][pj] = 1

        # 아래 두 칸에 모두 길이 있을 때
        if 0<=ci+1<N and not board[ci+1][cj] and not board[pi+1][pj]:
            if not visited[ci+1][cj] and not visited[pi+1][pj]:
                nxt.append((ci+1, cj, d))
            if not visited[ci+1][cj]:
                nxt.append((ci+1, cj, 1))
                visited[ci+1][cj] = 1
            if not visited[pi+1][pj]:
                nxt.append((pi+1, pj, 1))
                visited[pi+1][pj] = 1

    # 현재 새로 방향일 때
    else:
        # 좌 두칸에 모두 길이 있을 때
        if 0 <=cj-1<N and not board[ci][cj-1] and not board[pi][pj-1]:
            if not visited[ci][cj-1] and not visited[pi][pj-1]:
                nxt.append((ci, cj-1, d))
            if not visited[ci][cj-1]:
                nxt.append((ci, cj-1, 2))
                visited[ci][cj-1] = 1
            if not visited[pi][pj-1]:
                nxt.append((pi, pj-1, 2))
                visited[pi][pj-1] = 1
        # 우 두칸에 모두 길이 있을 때
        if 0 <=cj+1<N and not board[ci][cj+1] and not board[pi][pj+1]:
            if not visited[ci][cj+1] and not visited[pi][pj+1]:
                nxt.append((ci, cj+1, d))
            if not visited[ci][cj+1]:
                nxt.append((ci, cj+1, 3))
                visited[ci][cj+1] = 1
            if not visited[pi][pj+1]:
                nxt.append((pi, pj+1, 3))
                visited[pi][pj+1] = 1
    return nxt


def DFS(i, j, d, dis): # i, j: 현재위치 / d: 방향 / dis: 총 이동 거리
    global min_val, N
    # 종료조건: 오른쪽 끝에 도달했을때
    if i == N-1 and j == N-1:
        min_val = min(min_val, dis)
        return

    nxt = next_position(i, j, d)
    print(i, j, d, dis)
    for ni, nj, nd in nxt:
        visited[ni][nj] = 1
        DFS(ni, nj, nd, dis + 1)
        visited[ni][nj] = 0


# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
min_val = 9876543212

N = 0
visited = []
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# board = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def solution(b):
    global N, visited, board, min_val
    # board = b
    N = len(board)
    si, sj, sd = 0, 1, 3  # 시작점

    visited = [[0] * N for _ in range(N)]
    visited[0][1] = 1
    visited[0][0] = 1

    DFS(si, sj, sd, 0)
    return min_val

print(solution(board))