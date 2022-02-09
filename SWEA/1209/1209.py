# import sys
# sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    _ = input()
    # 0~99 가로줄의 합 100~199 세로줄의 합 200 우하향 대각선줄의 합 201 우상향 대각선줄의 합
    sums = [0] * 202
    for i in range(100):
        nums = list(map(int, input().split()))
        # 가로줄의 합
        sums[i] = sum(nums)
        # 우하향 대각선
        sums[200] += nums[i]
        # 우상향 대각선
        sums[201] += nums[99-i]
        # 세로줄에 하나 더하기
        for j in range(100):
            sums[100 + j] += nums[j]
    print(f'#{tc} {max(sums)}')