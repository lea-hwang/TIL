import sys
sys.stdin = open('1022_input.txt', 'r')

N = 3
matrix = [[0] * N for _ in range(N)]
d_rc = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 우상좌하

i = j = N//2
start = end = i
num = 2

matrix[i][j] = 1
while num <= N * N:
    for d in d_rc: # 우상좌하로 이동
        if d == (0, 1):
            start -= 1
            end += 1
        ni = i + d[0]
        nj = j + d[1]
        while start <= ni <= end and start <= nj <= end:
            i, j = ni, nj
            matrix[i][j] = num
            ni += d[0]
            nj += d[1]
            num += 1
print(matrix)