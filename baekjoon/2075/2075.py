import sys
sys.stdin = open("input.txt")
import heapq

N = int(input())

nums = list(map(int, sys.stdin.readline().rstrip().split()))


for i in range(1, N):
    new_nums = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if nums and new_nums[j] > nums[0]:
            heapq.heappush(nums, new_nums[j])
            heapq.heappop(nums)


print(nums[0])