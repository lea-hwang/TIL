import sys
sys.stdin = open('2805_input.txt', 'r')

N, M = map(int, input().split())  # 나무의 수, 나무의 길이
trees = list(map(int, input().split()))
# 1. 가장 긴 나무를 찾는다.
start = 0
end = max(trees)


def get_length(mid):
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    return total


def binary_search():
    global start, end, M
    while start <= end:
        mid = (start + end) // 2
        total = get_length(mid)
        if total < M:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

answer = binary_search()
print(answer)
