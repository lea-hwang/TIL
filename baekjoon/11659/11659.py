import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

nums = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, N+1):
    nums[i] = nums[i] + nums[i-1]

for time in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(nums[j] - nums[i-1])