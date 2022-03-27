import sys
sys.stdin = open('9020_input.txt', 'r')


def prime_number(N): # N까지의 소수리스트를 만든다.
    for i in range(2, N+1):
        if not prime[i]:
            continue
        for j in range(i+i, N+1, i):
            prime[j] = False


def find_partition(N):
    middle = N//2
    for idx in range(0, middle):
        if prime[middle - idx] and prime[middle + idx]:
            return [middle - idx, middle + idx]


T = int(input())
maximum = 10000
prime = [False] * 2 + [True] * (maximum-1)
prime_number(maximum) # 미리 만들기

for _ in range(T):
    N = int(input())
    print(*find_partition(N))

