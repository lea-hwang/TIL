def sequential(A, N, key):
    for i in range(N):
        if A[i] == key:
            return i
    else:
        return -1

A = [4, 8, 11, 23, 1, 2]
print(sequential(A, 6, 8))
print(sequential(A, 6, 10))