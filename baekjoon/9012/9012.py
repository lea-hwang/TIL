import sys
sys.stdin = open('9012_input.txt', 'r')

N = int(input())
for _ in range(N):
    PS = input()
    count = 0
    PVS = True
    for x in PS:
        if x == '(':
            count += 1
        else:
            if count == 0:
                PVS = False
                break
            else:
                count -= 1
    if not count and PVS:
        print('YES')
    else:
        print('NO')
