def subset(A, B, N):
    for i in range(1<<N):
        B.append([])
        for j in range(N):
            if i & (1<<j):
                B[i].append(A[j])


A = [3, 6, 7, 1, 5]
B =  []
subset(A, B, 5)
print(B)