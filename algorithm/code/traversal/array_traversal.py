def row_major_order(A, N):
    for i in range(N):
        for j in range(N):
            print(A[i][j])

def column_major_order(A, N):
    for j in range(N):
        for i in range(N):
            print(A[i][j])

def zigzag(A,N):
    for i in range(N):
        for j in range(N):
            print(A[i][j + (N - 1 - 2 * j)* (i%2)])

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# row_major_order(A, 3)
# column_major_order(A, 3)
zigzag(A, 3)
