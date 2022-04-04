import sys
sys.stdin = open('input.txt', 'r')

nums = list(map(int, input()))
cur = nums[0]
cnt = 1
for i in range(1, len(nums)):
    if cur != nums[i]:
        cnt += 1
        cur = nums[i]

print(cnt//2)