import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

total = 0
for i in range(N):
    total += nums[i] * (i+1)

print(total)
