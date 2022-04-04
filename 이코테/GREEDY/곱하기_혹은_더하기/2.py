import sys
sys.stdin = open('input.txt', 'r')

nums = list(map(int, input()))

total = 0
for i in range(len(nums)):
    if total == 0 or nums[i] == 0:
        total += nums[i]
    else:
        total *= nums[i]
print(total)