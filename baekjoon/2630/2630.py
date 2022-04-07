import sys
sys.stdin = open('input.txt', 'r')


def check(i, j, N):
    global blue, white
    num = mat[i][j]
    for p in range(i, i + N):
        for k in range(j, j + N):
            if mat[p][k] != num:
                return False
    if num:
        blue += 1
    else:
        white += 1
    return True

def paint(i, j, N): # 왼쪽 위 꼭짓점, 가로 길이
    if check(i, j, N):
        return
    paint(i, j, N//2)
    paint(i, j+N//2, N//2)
    paint(i+N//2, j, N//2)
    paint(i+N//2, j+N//2, N//2)


N = int(input())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
white = 0
blue = 0
paint(0, 0, N)
print(white)
print(blue)
