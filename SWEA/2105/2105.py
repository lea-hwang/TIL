import sys
sys.stdin = open('2105_input.txt', 'r')


def DFS(i, j, n, visited): #현재 위치, 현재 방향, 방문한 숫자 저장, 디저트 총합
    global si, sj, ans, N
    if n==2 and ans>=len(visited)*2:
        return
    # 종료조건
    if n > 3:
        return
    # 성공조건
    if n==3 and i==si and j==sj: # 처음 위치에 돌아왔을때,
        if ans < len(visited):
            ans = len(visited)
        return
    # 다음 좌표 찾기
    for k in range(n, n+2): # 방향 선택 -> 현재방향 or 회전
        n_i = i + d_rc[k][0]
        n_j = j + d_rc[k][1]
        # 인덱스를 벗어나지 않고, 디저트 번호가 중복되지 않을때,
        if 0<=n_i<N and 0<=n_j<N and mat[n_i][n_j] not in visited:
            visited.append(mat[n_i][n_j])
            DFS(n_i, n_j, k, visited)
            visited.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    d_rc = [(1, -1), (1, 1), (-1, 1), (-1, -1), (0, 0)] # 마지막 값은 더미.
    for si in range(0, N-2):
        for sj in range(1, N-1):
            DFS(si, sj, 0, [])
    print(f'#{tc} {ans}')