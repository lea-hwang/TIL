def bubble_sort(A, N):
    for i in range(1, N):
        for j in range(i, N):
            if A[j] < A[j-1]:
                A[j-1], A[j] = A[j], A[j-1]

A = [55, 7, 78, 12, 42]
bubble_sort(A, 5)
print(A)

