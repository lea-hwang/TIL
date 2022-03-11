import sys
sys.stdin = open('2178_input.txt', 'r')

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
start = (0,0)


def dfs(start, N, M): # 처음 위치 받기
    queue = [start] # 현재위치에서 갈 수 있는 길들을 저장할 큐, 처음 위치로 초기값 설정
    matrix[0][0] = 0
    d_rc = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 4방향
    while queue:
        i, j = queue.pop(0)
        
        if i == N-1 and j == M-1: # 현재 위치가 도착지이면, return 최소값
            return matrix[i][j]
        
        # 현재 위치에서 갈 수 있는 길(상우하좌) 스택에 모두 저장
        for d in d_rc:
            ni = i + d[0]
            nj = j + d[1]
            if 0<=ni<N and 0<=nj<M and (matrix[ni][nj] == 1): # 인덱스를 벗어나지 않고, 해당 칸의 값이 1일 때
                queue.append((ni, nj))
                matrix[ni][nj] = matrix[i][j] + 1
    return 0

print(dfs(start, N, M) + 1)