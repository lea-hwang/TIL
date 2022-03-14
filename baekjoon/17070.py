import sys
sys.stdin = open('17070_input.txt', 'r')

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# # 각 이동별 살펴야하는 위치
# d_check = {
#     'h': [(0, 1)],  # 수평이동
#     'v': [(1, 0)],  # 수직이동
#     'd': [(0, 1), (1, 0), (1, 1)],  # 대각선이동
# }
#
# # 현재 방향에 따른 갈 수 있는 다음 위치
# d_rc = {
#     'h': [(0, 1, 'h'), (1, 1, 'd')],
#     'v': [(1, 0, 'v'), (1, 1, 'd')],
#     'd': [(0, 1, 'h'), (1, 0, 'v'), (1, 1, 'd')],
# }
#
# cnt = 0

# def check(i, j, n_d): # 다음 이동 장소에서 주변이 비어있는지를 판단하는 함수
#     for d in d_check[n_d]:
#         if house[i + d[0]][j + d[1]] == '1': # 만약 벽이라면 return False
#             return False
#     return True


# def DFS(N):
#     global cnt
#     stack = [(0, 1, 'h')] # 현재 위치를 저장할 스택, 현재 위치 초기값 설정
#     while stack:
#         i, j, now_d = stack.pop()
#         for d in d_rc[now_d]: # 다음 이동할 수 있는 위치와 방향
#             n_i, n_j, n_d = i + d[0], j + d[1], d[2]
#             # 인덱스를 벗어나지 않으면서, 주변이 벽이 아닐때
#             if 0<=n_i<N and 0<=n_j<N and check(i, j, n_d):
#                 stack.append((n_i, n_j, n_d))
#                 if n_i == N - 1 and n_j == N - 1:
#                     cnt += 1
#                     break

def DP(N):
    matrix = [[[0]*3 for _ in range(N)] for _ in range(N)] # 좌, 상, 좌상 순으로 저장
    matrix[0][1] = [1, 0, 0]
    for i in range(N):
        for j in range(N):
            # 현재위치가 1이면 continue
            if house[i][j]: continue
            # 현재 위치를 기준으로 좌
            if (0 <= j-1) and (house[i][j-1] == 0):
                matrix[i][j][0] += matrix[i][j-1][0] + matrix[i][j-1][2]
            # 현재 위치를 기준으로 상
            if (0 <= i-1) and (house[i-1][j] == 0):
                matrix[i][j][1] += matrix[i-1][j][1] + matrix[i-1][j][2]
            # 현재 위치를 기준으로 좌상
            if (0 <= i-1) and (0 <= j-1) and (house[i-1][j] == 0 and house[i][j-1] == 0 and house[i-1][j-1] == 0):
                matrix[i][j][2] += matrix[i-1][j-1][0] + matrix[i-1][j-1][1] + matrix[i-1][j-1][2]
    return matrix[N-1][N-1]

if house[N-1][N-1] == '1':
    print(0)
else:
    # DFS(N)
    print(sum(DP(N)))
    #print(cnt)
