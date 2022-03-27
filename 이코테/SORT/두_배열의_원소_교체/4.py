import sys
sys.stdin = open('4_input.txt', 'r')

# 가장 작은 수, 가장 큰 수를 계속 찾아야하는 경우에는, 먼저 정렬을 하면 더 쉽게 찾을 수 있다!

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A, B 모두 정렬
A.sort()                    # 작은 수부터 정렬
B.sort(reverse=True)        # 큰 수부터 정렬


for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i]  # 크기가 다를 경우 바꾼다. -> 굳이 바꾸지 않아도 대입만해도 되긴함.

print(sum(A))





