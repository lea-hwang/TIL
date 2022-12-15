import sys
sys.stdin = open("1935_input.txt")
input = sys.stdin.readline

N = int(input().rstrip())

formula = input().rstrip()
nums = dict()

for n in range(0, N):
    letter = chr(65+n)
    nums[letter] = int(input().rstrip())

stack = []


calculate = {
    "+":lambda x, y: x + y,
    "-":lambda x, y: x - y,
    "*":lambda x, y: x * y,
    "/":lambda x, y: x / y,
}

for letter in formula:
    # 기호라면
    if letter in '+-/*':
        num2, num1 = stack.pop(), stack.pop()
        stack.append(calculate[letter](num1, num2))
    # 숫자라면
    else:
        stack.append(nums[letter])

print(f'{stack[-1]:.2f}')
