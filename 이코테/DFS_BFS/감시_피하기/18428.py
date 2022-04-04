import sys
sys.stdin = open('18428_input.txt', 'r')

N = int(input())  # 복도의 크기
mat = [input().split() for _ in range(N)]
Ts = []  # 선생님의 위치
Xs = []  # 아무것도 존재하지 않는 위치

# 선생님의 위치, 아무것도 존재하지 않는 위치 저장
for i in range(N):
    for j in range(N):
        if mat[i][j] == 'T':
            Ts.append((i, j))
        elif mat[i][j] == 'X':
            Xs.append((i, j))


# 아무것도 존재하지 않는 위치의 수 세기
len_X = len(Xs)


# 장애물 설치 및 제거 함수
def obstacle(letter, *Os):
    for oi, oj in Os:
        mat[oi][oj] = letter


# 선생님의 탐색 시작
def DFS():
    for ti, tj in Ts: # 모든 선생님 위치를 중심으로
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # 네 방향에서
            for k in range(N): # k 만큼 먼 거리에 학생이 있는 지 확인
                ni, nj = ti + di*k, tj + dj*k
                # 인덱스를 벗어나지 않을 때
                if 0<=ni<N and 0<=nj<N:
                    if mat[ni][nj] == 'S':
                        return False
                    elif mat[ni][nj] == 'O':
                        break
                else:
                    break
    return True

ans = "NO"
# 장애물 설치 후 탐색 시작
for o1 in range(len_X):
    for o2 in range(o1+1, len_X):
        for o3 in range(o2+1, len_X):
            # 장애물 3개 설치
            obstacle('O', Xs[o1], Xs[o2], Xs[o3])
            # 만약 학생이 감시를 피했을 때
            if DFS():
                ans = "YES"
                break
            # 장애물 3개 삭제
            obstacle('X', Xs[o1], Xs[o2], Xs[o3])

print(ans)

