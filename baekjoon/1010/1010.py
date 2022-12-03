import sys
sys.stdin = open("input.txt")

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    
    answer = factorial(M) // factorial(M-N) // factorial(N)
    print(answer)