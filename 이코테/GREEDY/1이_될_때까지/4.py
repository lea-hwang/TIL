import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

# N을 1로 만드는 최소 횟수
time = 0
while N > 1:
    if N % K: # 나머지가 있을 때
        N -= 1
    else:
        N //= K
    time += 1
print(time)