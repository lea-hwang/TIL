import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
input = sys.stdin.readline


def united(si, sj):
    global L, R
    # 시작점을 기준으로 갈 수 있는 모든 곳을 탐색
    # 해당 위치를 따로 저장해둠.
    visited[si][sj] = 1     # 현재 나라 방문
    queue = deque()         # 현재 나라 저장
    queue.append((si, sj))

    total = mat[si][sj]     # 연한합 나라의 인구 수 합
    union = [(si, sj)]      # 연합한 나라의 위치 저장
    cnt = 1                 # 연합한 나라의 수
    while queue:
        i, j = queue.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:   # 동서남북 중
            ni, nj = i + di, j + dj
            # 인덱스를 벗어나지 않고, 방문한 적이 없고,  현재 위치의 값과의 차이가 L, R 사이의 값일 때
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and L <= abs(mat[i][j] - mat[ni][nj]) <= R:
                queue.append((ni, nj))      # 다음 위치 저장
                visited[ni][nj] = 1         # 방문 표시
                total += mat[ni][nj]        # 다음 위치의 값을 더한다.
                cnt += 1                    # 연합한 나라의 수 += 1
                union.append((ni, nj))      # 연합한 나라의 위치 저장

    p_avg = total//cnt # 사람 평균
    if cnt == 1: # 주위와 연합하지 않았을 때
        return False
    else:
        for i, j in union: # 연합 국가들의 인구 수를 평균 인구수로 바꾼다.
            mat[i][j] = p_avg
        return True


N, L, R = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
day = 0

while True:
    visited = [[0] * N for _ in range(N)]   # 방문한 나라 저장
    not_united = 0                          # 연합하지 않은 나라의 수

    # 모든 좌표를 돌면서 연합을 찾아 평균 인구수를 구한다.
    for si in range(N):
        for sj in range(N):
            if visited[si][sj]:         # 이미 방문한 곳은 넘어감
                continue
            if not united(si, sj):      # 만약 연합하지 않았다면 not_united +1
                not_united += 1

    if not_united == N*N:  # 모든 나라가 연합되지 않았을 때
        break
    else:
        day += 1

print(day)

