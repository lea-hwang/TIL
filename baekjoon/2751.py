import sys
sys.stdin = open('2751_input.txt', 'r')

def merge(left, right):
    arr = []
    l=r=0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            arr.append(right[r])
            r += 1
        else:
            arr.append(left[l])
            l += 1
    arr += left
    arr += right
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

N = int(input())
arr = []
for _ in range(N):
    #num = int(sys.stdin.readline().strip())
    arr.append(int(input()))
arr = merge_sort(arr)
for i in range(N):
    print(arr[i])
