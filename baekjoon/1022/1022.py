import sys
sys.stdin = open('1022_input.txt', 'r')


r1, c1, r2, c2 = map(int, input().split())
N = max([abs(r1), abs(r2), abs(c1), abs(c2)]) # 제일 바깥 matrix의 크기
M = min([abs(c1), abs(c2)])
height = r2 - r1 + 1
width = c2 - c1 + 1
matrix = [[0] * width for _ in range(height)]
d_rc = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 우상좌하

i = j = N//2
start = end = i
num = M*M

matrix[i][j] = 1
while num <= N * N:
    for d in d_rc: # 우상좌하로 이동
        if d == (0, 1):
            start -= 1
            end += 1
        ni = i + d[0]
        nj = j + d[1]
        while num <= N * N and start <= ni <= end and start <= nj <= end:
            i, j = ni, nj
            matrix[i][j] = num
            ni += d[0]
            nj += d[1]
            num += 1
print(matrix)