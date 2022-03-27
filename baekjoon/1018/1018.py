def check_board(row, col):  # B, W 순으로 오는 체스판
    cnt = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if (i + j) % 2:  # i+j가 홀수일 때
                if board[i][j] == 'B':  # 'W'가 아닐때
                    cnt += 1
            else:  # 짝수일 때 -> 제일 첫번째 위치에서 한 칸씩 건너뛴 위치
                if board[i][j] == 'W':  # 'B'가 아닐때
                    cnt += 1
    return cnt

N, M = map(int, input().split())  # 행 열
board = [input() for _ in range(N)]  # 체스판
min_v = M * N  # 최솟값

# 8*8 체스판으로 쪼개기
for i in range(N - 7):
    for j in range(M - 7):
        # 체스판의 틀린 개수 찾기
        black = check_board(i,j)
        white = 64 - black
        min_v = min([black, white, min_v])
print(f'{min_v}')
