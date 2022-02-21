def selection_sort(A, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i, N):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

A = [64, 25, 10, 22, 11]
selection_sort(A, 5)
print(A)