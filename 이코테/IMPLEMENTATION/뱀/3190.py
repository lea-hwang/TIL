# 사과를 먹으면 뱀의 길이가 늘어난다.
# 벽 또는 자기 자신과 부딪히면 게임이 끝난다.

# N * N 정사각 보드, 사과 몇 개
# 상하좌우 끝에는 벽이 존재
# 시작시 뱀의 위치는 맨 왼쪽위에 위치, 뱀의 길이는 1이며 머리는 오른쪽을 향함.

# 이동 규칙
# 1. 먼저 머리를 늘려 한 칸 이동.
# 2. 이동한 칸에 사과가 있다면, 사과가 없어지고 꼬리의 위치는 그대로
# 3.             사과가 없다면, 꼬리가 위치한 칸을 비워줌

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수

board = [[0] * N for _ in range(N)]

# 사과 위치 저장
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    board[i-1][j-1] = 1

board[0][0] = 2     # 뱀 시작

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 우 하 좌
di = 1

positions = deque()
positions.append((0, 0))

def get_turn():
    global di, N
    turn = 1
    L = int(input()) # 뱀의 방향 변환 횟수
    for _ in range(L):
        X, C = sys.stdin.readline().split() # X초 뒤, 'L'(왼쪽) 'D'(오른쪽) 으로 회전
        X = int(X)
        while turn < X+1: # X초까지 이동하는데, 벽에 부딪히거나, 몸통과 부딪히지 않는지 살핀다.
            ci, cj = positions[-1]  # 현재 위치
            ni = ci + ds[di][0]
            nj = cj + ds[di][1]

            # 만약 다음 위치에 몸통이나 벽이 있다면 종료
            if (ni<0 or ni>=N) or (nj<0 or nj>=N) or board[ni][nj] == 2:
                return turn

            # 만약 다음 위치에 사과가 있다면 꼬리 위치 그대로 하고 머리만 이동
            elif board[ni][nj] == 1:
                positions.append((ni, nj))
                board[ni][nj] = 2

            # 만약 다음 위치에 아무것도 없다면 머리, 꼬리 한칸 이동
            else:
                positions.append((ni, nj)) # 머리 이동
                tail = positions.popleft() # 꼬리 이동
                board[ni][nj] = 2
                board[tail[0]][tail[1]] = 0

            turn += 1  # 횟수 증가

        # 뱀 이동 후 방향 전환
        if C == 'L': # 왼쪽으로 방향 전환
            di = (di-1 + 4) % 4
        else: # 오른쪽으로 방향 전환
            di = (di+1) % 4

    # 회전하는 동안 아무런 부딪힘이 없었을 때, 진행방향으로 계속 진행
    ci, cj = positions[-1]  # 현재 위치
    ni = ci + ds[di][0]
    nj = cj + ds[di][1]

    while (0<=ni<N) and (0<=nj<N) and board[ni][nj] != 2:
        ni = ni + ds[di][0]
        nj = nj + ds[di][1]
        turn += 1

    return turn


print(get_turn())