import sys
sys.stdin = open('1003_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    call_01 =[[0, 0] for _ in range(N+1)]
    call_01[0] = [1, 0]
    if len(call_01) > 1:
        call_01[1] = [0, 1]
    for i in range(2, N + 1):
        call_01[i][0] = call_01[i-1][0] + call_01[i-2][0]
        call_01[i][1] = call_01[i-1][1] + call_01[i-2][1]
    print(*call_01[N])
