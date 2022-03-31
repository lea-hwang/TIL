import sys
sys.stdin = open('14888_input.txt', 'r')


N = int(input())                                # 숫자의 개수
nums = list(map(int, input().split()))          # 숫자
ops = list(map(int, input().split()))           # 연산자의 개수: 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수


min_val = 1000000000
max_val = -1000000000

cal = {
    0: lambda x, y: x+y,
    1: lambda x, y: x-y,
    2: lambda x, y: x*y,
    3: lambda x, y: x//y if x>0 else -(-x//y),  # x가 음수일경우, 양수로 변환하여 계산후 다시 음수 변환
}

def dfs(k, N, answer):
    global min_val, max_val
    if k == N-1:
        min_val = min(min_val, answer)          # 최솟값 갱신
        max_val = max(max_val, answer)          # 최댓값 갱신
        return

    for i in range(4):
        if ops[i]:                              # 해당 연산자를 사용할 수 있을 때,(남아있을때)
            ops[i] -= 1
            dfs(k+1, N, cal[i](answer, nums[k+1]))
            ops[i] += 1

dfs(0, N, nums[0])

print(max_val)
print(min_val)
