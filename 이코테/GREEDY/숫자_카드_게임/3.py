import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())  # 행의 개수, 열의 개수
nums = [list(map(int, input().split())) for _ in range(N)]

# 각 행의 최솟값이 가장 큰 값을 찾아 출력
min_val = [0] * N
for i in range(N):
    min_val[i] = min(nums[i])

print(max(min_val))
