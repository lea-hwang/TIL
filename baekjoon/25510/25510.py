import sys
sys.stdin = open("input.txt")

T = int(input())

for i in range(T):
    line = input()
    N = len(line)
    left = 0
    right = N-1
    count = 1
    while left < right:
        if line[left] == line[right]:
            left += 1
            right -= 1
            count += 1
        else:
            break

    if left < right:
        print(0, count)
    else:
        print(1, count)