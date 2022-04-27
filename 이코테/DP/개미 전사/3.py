# 만약 현재 창고 번호가 i일 때,
# i-1 번째까지의 누적합보다
# i-2번째와 i번째 창고의 식량이 더 많은 것을 골라 턴다

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
foods = list(map(int, input().split()))
dp = [0] * N

dp[0] = foods[0]
dp[1] = max(foods[0], foods[1])

for i in range(2, N):
    dp[i] = max(dp[i-2] + foods[i], dp[i-1])

print(dp[-1])