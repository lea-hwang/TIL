import sys
sys.stdin = open('15684_input.txt', 'r')


N, M, H = map(int, input().split())  # 세로선의 개수, 가로선의 개수, 세로선마다 놓을 수 있는 가로선의 개수
h_lines = [[0] * (N+2) for _ in range(H+1)] # (H+1)*(N+2) 행렬


# 나중에 다시 풀기 퓨
