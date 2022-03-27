import sys
sys.stdin = open('2_input.txt', 'r')

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)
print(*nums)