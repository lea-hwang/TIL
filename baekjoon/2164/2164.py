import sys
sys.stdin = open('2164_input.txt', 'r')

N = int(input())
nums = [i for i in range(1, N+1)]
while len(nums) > 1:
    if len(nums) % 2: # 홀수
        nums = [nums[-1]] + nums[1:N:2]
    else:
        nums = nums[1:N:2]
print(*nums)

