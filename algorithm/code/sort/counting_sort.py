def counting_sort(A, B, N):
    counts = [0] * (N+1)
    for num in A: # 각 숫자 개수 구하기
        counts[num] += 1
    for i in range(1, N+1): # 각 숫자 누적 구하기
        counts[i] = counts[i-1] + counts[i]
    for num in A[::-1]: # counts에 1을 빼고 해당 숫자를 B에 넣는다.
        counts[num] -= 1
        B[counts[num]] = num
        

A = [0, 4, 1, 3, 2, 4, 1]
B = [0, 0, 0, 0, 0, 0, 0]
counting_sort(A, B, 5)
print(B)