import sys
sys.stdin = open('15652_input.txt', 'r')

def sequence(N, M, pre):
    if M == 0:
        print(*nums)
        return
    for i in range(pre, N+1):
        nums.append(i)
        sequence(N, M-1, i)
        nums.pop()


N, M = map(int, input().split())
nums = []
sequence(N, M, 1)
