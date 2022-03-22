import sys
sys.stdin = open('14502_input.txt', 'r')


N, M = map(int, input().split()) # 세로크기, 가로크기
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0: 빈칸, 1: 벽, 2: 바이러스

# 브루트포스
#
for w1 in range(N * M): # 첫번째 놓을 벽
    for w2 in range(d1 + 1, N * M): # 두번째 놓을 벽
        for w3 in range(d2 + 1, N * M): # 세번째 놓을 벽
            
