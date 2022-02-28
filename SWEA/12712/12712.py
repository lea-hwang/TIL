import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    d1 = [(1,0), (-1,0), (0,1), (0,-1)]
    d2 = [(-1,-1), (-1,1), (1,-1), (1,1)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            s1 = s2 = flies[i][j]
            for k in range(4): # 방향
                for l in range(1, M): # 거리
                    # 십자형
                    ni1, nj1 = i + d1[k][0]*l, j + d1[k][1]*l
                    if 0 <= ni1 < N and 0 <= nj1 < N:
                        s1 += flies[ni1][nj1]

                    # 대각선
                    ni2, nj2 = i + d2[k][0]*l, j + d2[k][1]*l
                    if 0 <= ni2 < N and 0 <= nj2 < N:
                        s2 += flies[ni2][nj2]

            max_v = max([max_v, s1, s2])

    print(f'#{tc} {max_v}')