# 유형: 그리디
# 풀이방법:
# 가장 큰 수(B)와 가장 작은 수(A)가 만나도록 조정


import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for i in range(N):
    A.sort()
    B.sort(key=lambda x: -x)
    result += A[i] * B[i]

print(result)
