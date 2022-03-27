import sys
sys.stdin = open('9095_input.txt', 'r')

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    dp_list = [0] * (N+1)
    dp_list[1] = 1
    dp_list[2] = 2
    dp_list[3] = 3
    print(f' ')