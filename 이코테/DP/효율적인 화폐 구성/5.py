import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())  # 화폐 종류, 목표 금액
dp = [10001] * (M+1)
coins = [] # 각 확페 금액

for i in range(N):
    coins.append(int(input()))

dp[0] = 0

for i in range(M+1):
    for coin in coins:
        if i >= coin and dp[i-coin] != 10001:
            dp[i] = min(dp[i], dp[i-coin] + 1)
if dp[M] != 10001:
    print(dp[M])
else:
    print(-1)