import sys
sys.stdin = open("input.txt")

S = input()

cur = ''
count = 0
for num in S:
    if num != cur:
        count += 1
    cur = num

print(count//2)