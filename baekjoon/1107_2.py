import sys

sys.stdin = open('1107_input.txt', 'r')

N = input()  # 이동하려는 채널
N_list = list(map(int, N))
M = int(input())  # 고장난 버튼의 개수
not_btns = set(map(int, input().split()))  # 누를 수 없는 버튼
btns = list(set([i for i in range(10)]) - not_btns)  # 누를 수 있는 버튼
# 누를 수 있는 숫자들로 숫자 만들기
def permutation(N, M, first): # 전체 숫자 개수, M 고를 숫자의 개수
    if M == 0:
        a = first
        for i in range(len(nums)):
            a = a * 10 + nums[i]
        num_list.append(a)
        return
    for i in range(10):
        if i not in btns: continue
        nums.append(i)
        permutation(N, M-1, first)
        nums.pop()

picked = [0] * len(btns) # 넣은 숫자
nums = []       # 누를 수 있는 숫자들로 만들어진 숫자
num_list = []   # 만들어진 숫자들의 집합

for i in range(0, 10):
    if i not in btns: continue
    permutation(len(btns), len(N_list) - 1, i)
    permutation(len(btns), len(N_list), i)

min_v = 500000
min_idx = 0
for i in range(len(num_list)):
    diff = abs(int(N) - num_list[i])
    if diff < min_v:
        min_v = diff
        min_idx = i
# print(min_idx)
print(num_list)
# print(min_v + len(str(num_list[min_idx])))

if abs(100 - int(N)) <= min_v:
    print(abs(100 - int(N)))
else:
    print(min_v + len(str(num_list[min_idx])))