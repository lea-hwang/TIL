import sys
sys.stdin = open('1654_input.txt', 'r')

K, N = map(int, input().split()) # 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
lines = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
start = 1
end = max(lines)


def cut_line(mid):
    global K
    total = 0
    for i in range(K):
        total += lines[i]//mid
    return total

def binary_search():
    global start, end, N
    while start <= end:
        mid = (start + end)//2
        total = cut_line(mid)
        if total < N:           # 잘린 랜선의 개수가 부족
            end = mid -1
        else:
            result = mid
            start = mid + 1
    return result

answer = binary_search()
print(answer)