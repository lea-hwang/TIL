import sys
sys.stdin = open('1767_input.txt', 'r')


def check(i, j, d, N): # 현재 방향에 코어나 전선이 있는지 여부 확인
    n_i, n_j = i, j
    while True:
        n_i, n_j = n_i + d[0], n_j + d[1]
        # 인덱스를 벗어나지 않을때,
        if 0<=n_i<N and 0<=n_j<N:
            # 코어나 전선이 있을 경우
            if cells[n_i][n_j]: return False
        else: return True


def line_connect(i, j, d, N):
    line = 0
    n_i, n_j = i, j
    while True:
        n_i, n_j = n_i + d[0], n_j + d[1]
        # 인덱스를 벗어나지 않을때, 전선을 넣어준다
        if 0<=n_i<N and 0<=n_j<N:
            cells[n_i][n_j] = 2
            line += 1
        else: return line

def line_disconnect(i, j, d, N):
    line = 0
    n_i, n_j = i, j
    while True:
        n_i, n_j = n_i + d[0], n_j + d[1]
        # 인덱스를 벗어나지 않을때, 전선을 넣어준다
        if 0<=n_i<N and 0<=n_j<N:
            cells[n_i][n_j] = 0
            line += 1
        else: return line


def connection(k, core, line, N):
    global core_line
    # 연결한 코어의 수가 많거나, 코어의 수는 같은데 연결한 전선의 길이가 짧다면 core_line을 갱신한다
    if (core > core_line[0]) or (core == core_line[0] and line < core_line[1]):
        core_line = [core, line]

    if k == len(cores):
        return

    # k번째의 코어를 연결가능 여부 파악을 위해
    i, j = cores[k] # k번째 코어의 위치
    d_rc = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 우 하 좌
    # 상우하좌를 모두 살핀다 -> 코어가 있는지, 전선이 있는지 모두 살핀다음
    for d in d_rc:
        if check(i, j, d, N):
            line += line_connect(i, j, d, N) # 코어에 전선을 연결하고 그 전선 길이를 더해주기
            core += 1 # 코어 수 +1
            connection(k+1, core, line, N) # 다음 코어 연결하기
            line -= line_disconnect(i, j, d, N) # 코어에 전선을 해제하고 그 전선 길이 빼주기
            core -= 1 # 코어 수 -1

    # 연결이 불가능하다면 연결하지 않고 다음 코어를 살핀다
    connection(k+1, core, line, N)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cells = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    core_line = [0, 0] # 연결된 코어 수, 라인길이

    # 가장자리에 위치한 코어 세기
    core_line[0] += cells[0].count(1) + cells[N-1].count(1) # 제일 위쪽과 아래쪽에 코어 수 더해주기
    for i in range(N):
        # 왼쪽 라인에 코어가 위치할 경우
        if cells[i][0]: core_line[0] += 1
        # 오른쪽 라인에 코어가 위치할 경우
        if cells[i][N-1]: core_line[0] += 1

    # 안쪽에 있는 코어 위치 찾기
    for i in range(1, N-1):
        for j in range(1, N-1):
            if cells[i][j]: cores.append((i, j))

    connection(0, core_line[0], core_line[1], N)

    print(f'#{tc} {core_line[1]}')

