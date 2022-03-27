import sys
sys.stdin = open('10989_input.txt', 'r')

N = int(input())
nums = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    nums[num] += 1
for i in range(1, 10001):
    for j in range(nums[i]):
        print(i)

# 시간 초과때문에, sys.stdin.readline() 사용, 카운트 정렬 이용

