# # 흰돌을 사용안한 것, 흰돌을 사용한것을 순서대로.
# DP_row = [[[0, 0] for _ in range(N+2)] for _ in range(N+2)]
# DP_col = [[[0, 0] for _ in range(N+2)] for _ in range(N+2)]
# DP_right = [[[0, 0] for _ in range(N+2)] for _ in range(N+2)] # 우하향
# DP_left = [[[0, 0] for _ in range(N+2)] for _ in range(N+2)]  # 좌하향
#
# max_val = 0
# # 검은 돌만 가지고 있는 상태에서 DP, 최대값 구하기
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if board[i-1][j-1] == 1:
#             DP_row[i][j][0] += DP_row[i][j-1][0] + 1
#             DP_row[i][j][1] += DP_row[i][j-1][1] + 1
#             DP_col[i][j][0] += DP_col[i-1][j][0] + 1
#             DP_col[i][j][1] += DP_col[i-1][j][1] + 1
#             DP_right[i][j][0] += DP_right[i-1][j-1][0] + 1
#             DP_right[i][j][1] += DP_right[i-1][j-1][1] + 1
#             DP_left[i][j][0] += DP_left[i-1][j+1][0] + 1
#             DP_left[i][j][1] += DP_left[i-1][j+1][1] + 1
#         elif board[i-1][j-1] == 2:
#             DP_row[i][j][1] += DP_row[i][j - 1][0] + 1
#             DP_col[i][j][1] += DP_col[i - 1][j][0] + 1
#             DP_right[i][j][1] += DP_right[i - 1][j - 1][0] + 1
#             DP_left[i][j][1] += DP_left[i - 1][j + 1][0] + 1
#         max_val = max([max(DP_row[i][j]), max(DP_col[i][j]), max(DP_right[i][j]), max(DP_left[i][j]), max_val])
#
# print(max_val)
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

r = [[] for _ in range(N)]
d = [[] for _ in range(N)]
r_d = [[] for _ in range(N)]
l_d = [[] for _ in range(N)]

for i in range(N):
    total = 0
    total1 = 0
    for j in range(N):
        # row 접근
        if board[i][j] == 1:
            total += 1
        elif board[i][j] == 2:
            if total:
                r[i].extend([total, -1])
                total = 0
            else:
                r[i].append(-1)
        else:
            if total:
                r[i].extend([total, 0])
                total = 0
            else:
                r[i].append(0)

        # col 접근
        if board[j][i] == 1:
            total1 += 1
        elif board[j][i] == 2:
            if total1:
                d[i].extend([total1, -1])
                total1 = 0
            else:
                d[i].append(-1)
        else:
            if total1:
                d[i].extend([total1, 0])
                total1 = 0
            else:
                d[i].append(0)
    if total:
        r[i].append(total)
    if total1:
        d[i].append(total1)
print(r)
print(d)



