import sys
sys.stdin = open("input.txt")

T = int(input())

for test in range(T):
    N = int(input())
    first = input()
    last = input()

    total = 0
    W = 0
    work = 0 
    for i in range(N):
        if first[i] != last[i]:
            total += 1
            if first[i] == 'W':
                W += 1
    if W > total//2:
        W = total - W
    work = W + (total - W * 2)
    print(work)    