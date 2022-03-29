import sys
sys.stdin = open('2_input.txt', 'r')

N = int(input())
components = list(map(int, input().split()))
M = int(input())
demands = list(map(int, input().split()))

components.sort()  # 오름차순으로 정렬


def binary_search(target):
    start = 0
    end = N
    while start < end:
        middle = (start + end) // 2
        if components[middle] == target:   # 숫자를 찾았을 때
            return True
        elif components[middle] > target:  # 가운데에 있는 숫자보다 더 작을 때
            end = middle -1
        else:                           # 가운데에 있는 숫자보다 더 클때
            start = middle + 1
    return False



for demand in demands:
    if binary_search(demand):
        print('yes', end=' ')
    else:
        print('no', end=' ')