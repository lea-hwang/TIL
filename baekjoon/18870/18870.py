import sys
sys.stdin = open('18870_input.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))

new_nums = sorted(list(set(nums)))

num_dic = dict()
for i in range(len(new_nums)):
    num_dic[new_nums[i]] = i

for num in nums:
    print(num_dic[num], end=" ")

