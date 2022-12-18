import sys
sys.stdin = open("input.txt")

N = int(input())

nums = list(map(int, input().split()))

K = int(input())

print(nums.count(K))