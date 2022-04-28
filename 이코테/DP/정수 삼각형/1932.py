import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
dp = [[0] * N for _ in range(N)]
for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(len(nums)):      # 현재 레벨의 각 수에 대하여
        # 이전 레벨의 왼쪽 수와 오른쪽 수를 비교하여 큰 값을 더해준다.
        left = 0
        if j-1 < i+1:
            left = dp[i-1][j-1]
        right = dp[i-1][j]
        dp[i][j] = nums[j] + max(left, right)

max_val = 0
for j in range(N):
    max_val = max(max_val, dp[N-1][j])

print(max_val)