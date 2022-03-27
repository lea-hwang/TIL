import sys
sys.stdin = open('1436_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    i = 0
    num = 1
    while i < N:
        if '666' in str(num):
            i += 1
            if i == N:
                break
        num += 1
    print(f'#{tc} {num}')