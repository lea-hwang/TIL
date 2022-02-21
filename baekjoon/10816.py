import sys
sys.stdin = open('10816_input.txt', 'r')

N = int(input())
nums = dict()

num_list = list(map(int, input().split()))
for curr in num_list:
    nums[curr] = nums.get(curr, 0) + 1
M = int(input())
picked = list(map(int, input().split()))
for num in picked:
    print(nums.get(num, 0), end=' ')
print()