import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
balls = list(map(int, input().split()))

W = [0] * (M+1)  # 각 무게별로 공의 개수
for i in range(N):
    W[balls[i]] += 1

case = 0
total_cnt = sum(W)
for i in range(1, M):
    total_cnt -= W[i]
    case += W[i] * total_cnt

print(case)