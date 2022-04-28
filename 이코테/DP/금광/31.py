import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())  # n*m
    nums = list(map(int, input().split()))
    matrix = [nums[i*m:i*m+m] for i in range(n)]
    dp = [[0] * m for _ in range(n)]

    for j in range(m):
        for i in range(n):
            if j == 0:
                dp[i][j] = matrix[i][j]
            else:
                for k in (i-1, i, i+1):
                    if 0 <= k < n:
                        dp[i][j] = max(dp[i][j], dp[k][j-1] + matrix[i][j])
    max_val = 0
    for i in range(n):
        max_val = max(max_val, dp[i][m-1])
    print(max_val)
