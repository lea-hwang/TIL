import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
A = set()
B = set()

for _ in range(N):
    A.add(input())

for _ in range(M):
    B.add(input())

C = list(A & B)
C.sort()
print(len(C))
for name in C:
    print(name)