import sys
sys.stdin = open("input.txt")

N = int(input()) # 나무의 개수

default = list(map(int, input().split()))

grow = list(map(int, input().split()))


total = sum(default)


for idx, value in enumerate(sorted(grow)):
    total += value * (idx)

print(total)