import sys
sys.stdin = open('16637_input.txt', 'r')

N = int(input()) # 식의 길이
f = input() # 식
ops = [] # 연산자를 저장할 리스트
nums = [] # 숫자를 저장할 리스트
for letter in f:
    # 만약 연산자라면 ops에 추가
    if letter in '+*-': 
        ops.append(letter)
    # 만약 숫자라면 nums에 추가
    else:
        nums.append(int(letter))


is_p = [0] * len(ops) # 괄호 여부
max_val = -2 ** 31 - 1 # 최댓값

# 각 연산자 별 계산식
operation = {
    '+': lambda x, y : x+y,
    '-': lambda x, y : x-y,
    '*': lambda x, y : x*y,
}

def calculation(N):
    num = nums[0]
    i = 0
    while i < N:
        if i+1<N and is_p[i+1]: # 뒤의 식이 먼저 처리해야할 때(괄호가 있을때)
            a, b = nums[i+1], nums[i+2]
            c = operation[ops[i+1]](a, b)
            num = operation[ops[i]](num, c)
            i += 2
        else:
            num = operation[ops[i]](num, nums[i+1])
            i += 1
    return num


def set_order(k, N):
    global max_val
    if k >= N:
        c = calculation(N)
        max_val = max(c, max_val)
        return
    if (k == 0) or (is_p[k-1] == 0 and is_p[k] == 0):
        is_p[k] = 1
        set_order(k + 2, N)
    is_p[k] = 0
    set_order(k + 1, N)


set_order(0, len(ops))
print(max_val)

