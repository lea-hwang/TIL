import sys
sys.stdin = open('2447_input.txt', 'r')


def blank(i, j, N): #왼쪽 위 좌표
    if N == 1:
        return
    # 만약 (i//3)
    for x in range(i, i+N, N//3):
        for y in range(j, j+N, N//3):
            if x == i + N//3 and y == j+ N//3:
                continue
            blank(x, y, N//3)
    for x in range(i + N//3, i + N//3*2):
        for y in range(j + N//3, j + N//3*2):
            star[x][y] = ' '

N = int(input()) # 3의 거듭제곱
star = [['*'] * N for _ in range(N)]
blank(0, 0, N)
for i in range(N):
    print(''.join(star[i]))