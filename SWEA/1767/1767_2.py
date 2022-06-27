# 풀이시간: 1시간 34분
# 시간: 8초
# 메모리: 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

# 풀이 방법
## 모든 코어를 동, 서, 남, 북 방향에 대해서 연결하면서 최대로 연결할 수 있는 코어의 수 파악
## DFS로 접근. 한 코어가 연결되면 그 다음 코어를 연결하는 방식. -> 재귀로 구현

# 함수 설계
## 1. solution: 각각의 경우의 수에 대해서 다른 함수들을 추가적으로 실행할 함수. 최대 코어 수 리턴
## 2. core_connect_possible: 코어 연결이 가능한지 파악하는 함수
## 3. core_connection: 코어를 연결하는 함수
## 4. core disconnection: 코어 연결을 해제하는 함수

# 생각해본 것들.
## 1. 가장자리에 있는 모든 코어는 이미 연결되어 있다고 가정하여 미리 제외 -> 안하면 시간 초과 발생
## 2. 전역 변수로 뺄 수 있는 것들은 그냥 전역변수로 뺄 것...
## 3. DFS의 종료조건 잘 생각하기
## 4. 코어 연결이 불가능할 때, 아니면 일부러 연결하지 않을 때를 고려할 때 for 문 밖으로 빼야함... 
##    그렇지 않으면 모든 포문(동서남북)에서 돌아가게 됨..

# 느낀점
## DFS 공부 다시 열심히 하자...
## 항상 모든 코드는 설계대로만 하면 잘 될 거라 생각하지만 수정이 필요하다...ㅠㅠ

import sys
sys.stdin = open('1767_input.txt', 'r')

input = sys.stdin.readline
T = int(input()) # 테스트 케이스 수

# 전역변수 설정
mat = []
cores = []
N = 0
C = 0


# 코어를 연결할 수 있는지 여부 파악
def core_connect_possible(i, j, di, dj):
    ni, nj = i, j
    while True:
        ni += di
        nj += dj
        if 0<=ni<N and 0<=nj<N:
            # 해당 mat에 코어나 전선이 있을 때 return False
            if mat[ni][nj]:
                return False
        # 인덱스를 벗어났을 때 return True
        else:
            return True

# i, j에 위치한 코어 di, dj 방면으로 연결
def core_connection(i, j, di, dj):
    ni, nj = i, j
    line_len = 0
    while True:
        ni += di
        nj += dj
        if 0 <= ni < N and 0 <= nj < N:
            mat[ni][nj] = 2
            line_len += 1
        # 인덱스를 벗어났을 때 return 라인값
        else:
            return line_len

# i, j에 위치한 코어 연결 해제
def core_disconnection(i, j, di, dj):
    ni, nj = i, j
    while True:
        ni += di
        nj += dj
        if 0 <= ni < N and 0 <= nj < N:
            mat[ni][nj] = 0
        # 인덱스를 벗어났을 때
        else:
            return


# checked_core: 현재까지 확인된 코어의 수
# core: 현재까지 연결된 코어의 수
# line: 현재까지 연결된 라인의 길이
def solution(checked_core, core, line):
    global core_line
    
    # 갱신 조건
    # 현재까지 연결된 코어의 수가 더 높거나, 더 적은 라인이 연결되었을 때,
    if (core_line[0] < core) or (core_line[0] == core and line < core_line[1]):
        core_line = [core, line]
    
    # 종료 조건
    # 만약 모든 core를 확인했을 때 return
    if checked_core == C:
        return

    i, j = cores[checked_core] # 현재 코어의 위치
    # DFS로 모든 core의 동서남북 방면에 전선연결해보기
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if core_connect_possible(i, j, di, dj):
            cur_line = core_connection(i, j, di, dj)
            solution(checked_core + 1, core + 1, line + cur_line)
            core_disconnection(i, j, di, dj)

    # 연결이 불가능 혹은 연결하지 않을 때 확인(for문 밖으로 빼야함)
    solution(checked_core + 1, core, line)


for tc in range(1, T+1):
    # 1. 입력값 받기
    N = int(input()) # 멕시노스의 크기 N * N
    mat = [list(map(int, input().split())) for _ in range(N)] # N*N 멕시노스

    core_line = [0, 0]  # 최대 코어 수, 최소 라인 길이
    cores = [] # 코어 위치 정보

    # 2. 해 찾기 전 세팅. - 코어의 위치 저장 및 총 개수 확인
    for i in range(N):
        for j in range(N):
            if mat[i][j]:
                if i == 0 or i == N-1 or j == 0 or j == N-1: # 가장자리에 있는 코어 제외.
                    core_line[0] += 1
                else:
                    cores.append((i, j)) # 코어의 위치 저장
    C = len(cores) # 전체 코어의 수

    # 3. 해 찾기
    solution(0, core_line[0], 0)

    print(f'#{tc} {core_line[1]}')

