import sys
sys.stdin = open('3_input.txt', 'r')


N, M = map(int, input().split())        # 떡의 개수, 요청한 떡의 길이
RC = list(map(int, input().split()))    # 떡의 길이

# 1. 가장 긴 떡의 길이를 구한다.
LENGTH = max(RC)

# 2. 현재 떡 길이를 기준으로 중간을 자르면서 요청한 떡의 길이와 비교한다(이진 탐색)
def cut_RC(p):
    total = 0
    for rc in RC:
        if rc > p:
            total += rc - p
    return total


def binary_search(start, end):
    result = 0
    while start <= end:
        middle = (start + end) // 2
        total = cut_RC(middle)
        if total < M:
            end = middle - 1
        else:
            start = middle + 1
            result = middle
    return result


print(binary_search(0, LENGTH))
