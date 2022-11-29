import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
A = []

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    new = list(map(int, input().split()))
    for j in range(M):
        A[i][j] += new[j]
    print(*A[i])
