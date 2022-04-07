import sys
sys.stdin = open('input.txt', 'r')

def z(row, col, M): # 왼쪽 위 좌표 M*M 행렬
    global cnt
    if M == 2:
        for i in range(2):
            for j in range(2):
                ni, nj = row+i, col+j
                cnt += 1
                if ni == r and nj == c:
                    print(cnt)
                    sys.exit(0)
    else:
        if r < row+M//2:
            if c < col+M//2:
                z(row, col, M//2)
            else:
                cnt += (M*M)//4
                z(row, col+M//2, M//2)

        else:
            cnt += (M*M)//2
            if c < col+M//2:
                z(row+M//2, col, M//2)

            else:
                cnt += (M*M)//4
                z(row+M//2, col+M//2, M//2)


N, r, c = map(int, input().split())
cnt = -1
z(0, 0, 2**N)
