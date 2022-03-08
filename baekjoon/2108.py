import sys
sys.stdin = open('2108_input.txt', 'r')


N = int(input())
nums = [0] * 8001
total = 0
for _ in range(N):
    num = int(input())
    nums[num + 4000] += 1
    total += num

# 산술 평균
print(round(total/N))

# 중앙값
center = N//2 + 1
cnt = 0
for i in range(8001):
    cnt += nums[i]
    if cnt >= center:
        print(i-4000)
        break

# 최빈값
top_cnt = max(nums)
top_num = 4001
for i in range(8001):
    if nums[i] == top_cnt:
        if top_num != 4001:
            top_num = i - 4000
            break
        else:
            top_num = i - 4000
print(top_num)

# 범위
min_num = 0
max_num = 0
for i in range(8001):
    if nums[i]:
        min_num = i-4000
        break
for j in range(8000, -1, -1):
    if nums[j]:
        max_num = j-4000
        break
print(max_num - min_num)