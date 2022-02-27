import sys
sys.stdin = open('1541_input.txt', 'r')

formula = input().replace('-', ' - ').replace('+', ' + ').split()
nums = []
operators = []
for i in range(len(formula)): # nums와 operators로 나눠서 넣어줌
    if formula[i] == '+' or formula[i] == '-':
        operators += formula[i]
    else:
        nums += [int(formula[i])]

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

# - 뒤에 있는 + 연산자를 먼저 계산해준다.
while len(nums) > 1:
    if operators[0] == '-':
        while len(nums) > 2 and operators[1] == '+': # -뒤에 + 연산자가 온다면 먼저 더해줌
            tmp = nums.pop(2)                     # 뒤에 있는 숫자 pop
            nums[1] = ops['+'](nums[1], tmp)  # 두 숫자 더해주기
            operators.pop(1)                      # + 연산자 제거
    tmp = nums.pop(1)
    nums[0] = ops[operators[0]](nums[0], tmp)
    operators.pop(0)

print(nums[0])
