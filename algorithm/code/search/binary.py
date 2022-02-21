def binary(A, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end)//2
        if A[middle] > key: # 가운데 위치한 값보다 더 작다면
            end = middle - 1
        elif A[middle] < key:
            start = middle + 1
        else:
            return True
    return False

A =[i for i in range(1, 11)]
print(binary(A, 10, 7))
