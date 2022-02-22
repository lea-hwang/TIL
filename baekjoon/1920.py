import sys
sys.stdin = open('1920_input.txt', 'r')

def binary(A, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if A[middle] == key:
            return 1
        elif A[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0

N = int(input())
N_nums = list(map(int, input().split()))
N_nums.sort()

_ = int(input())
M_nums = list(map(int, input().split()))

for num in M_nums:
    print(binary(N_nums,num))