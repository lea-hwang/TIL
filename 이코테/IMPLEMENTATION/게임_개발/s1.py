import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
si, sj, sd = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 1         # 이동 횟수
turn = 0        # 회전 횟수
cur_d = sd      # 현재 방향
i, j = si, sj   # 현재 위치
visited[i][j] = 1
while turn < 4:
    # 왼쪽으로 회전
    turn += 1
    cur_d = (4 + cur_d - turn) % 4
    # 길이 있고 가보지 않았고, 인덱스를 벗어나지 않을 때
    ni, nj = i + d[cur_d][0], j + d[cur_d][1]
    if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and not mat[ni][nj]:
        visited[ni][nj] = 1
        cnt += 1
        turn = 0
        i, j = ni, nj

print(cnt)