import sys
sys.stdin = open('15651_input.txt', 'r')


def permut_w_repeat(N, M):
    if M == 0:
        print(*nums)
        return
    for i in range(1, N+1):
        nums.append(i)
        permut_w_repeat(N, M-1)
        nums.pop()

N, M = map(int, input().split())
nums = []
permut_w_repeat(N, M)