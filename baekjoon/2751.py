import sys
sys.stdin = open('2751_input.txt', 'r')


def partition(start, end):
    if start >= end:
        return
    pivot = start
    left, right = start +1, end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right >= start and arr[right] > arr[pivot]:
            right += 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    def quick_sort(start, end):
        p_index = partition(start, end)
        quick_sort(start, p_index -1)
        quick_sort(p_)

N = int(input())
arr = [0] * N
for i in range(N):
    #num = int(sys.stdin.readline().strip())
    arr[i] = int(input())
quick_sort(0, N-1)
print(arr)

# for i in range(N):
#     print(arr[i])
