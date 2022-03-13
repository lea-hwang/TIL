import sys
sys.stdin = open('12852_input.txt', 'r')

N = int(input())

cnt = 0
results = [N]
while N > 1:
    if N % 3 == 0:
        results.append(N//3)
        N //= 3
    elif N % 9 == 1 and N % 4 and N % 6:
        results.append(N-1)
        N -= 1
    elif N % 2 == 0:
        results.append(N//2)
        N //= 2
    else:
        results.append(N-1)
        N -= 1
    cnt += 1
print(cnt)
print(*results)
