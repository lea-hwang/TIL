import sys
sys.stdin = open("input.txt")

from itertools import permutations

N, M = map(int, input().split())

nums = list(map(int, input().split()))
answers = list(permutations(sorted(nums), M))

for answer in answers:
    print(*answer)