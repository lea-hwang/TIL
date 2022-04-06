import sys
sys.stdin = open('9372_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input()) # 국가의 수, 비행기 종류
    airplanes = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        airplanes[a][b] = 1
        airplanes[b][a] = 1




    print(f'#{tc} ')