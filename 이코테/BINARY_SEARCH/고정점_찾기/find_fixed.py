import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid

        # arr 안에 있는 값이 인덱스보다 작을 경우 오른쪽 탐색(왼쪽은 무시해도 됨) -15 -6 1 3 7
        elif arr[mid] < mid:
            start = mid + 1

        # arr 안에 있는 값이 인덱스보다 클 경우 왼쪽 탐색(오른쪽은 무시해도 됨) -15 -4 2 8 9 13 15
        else:
            end = mid - 1
    return -1


print(binary_search(0, N-1))