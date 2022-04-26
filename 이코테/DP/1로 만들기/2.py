

# 5로 나누어 떨어지면 5로 나눈다
# 3으로 나누어떨이지면, 3으로 나눈다
# 2로 나누어떨어지면, 2로 나눈다
# x에서 1을 뺀다

# 1 2 3 4 5 6 7 8 ...
target = int(input())

dp = [0] * 30001
dp[1] = 1

for i in range(2, 30001):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)


print(dp[target] - 1)