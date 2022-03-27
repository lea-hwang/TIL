import sys

sys.stdin = open('1935_input.txt', 'r')

N = int(input()) # 문자의 개수
pro = input() # 후위 표현식
num_dic = {}
nums = []

for i in range(N):
    num = int(input())
    num_dic[chr(ord('A') + i)] = num

for char in pro:
    # 입력된 문자가 대문자일 경우
    if char in num_dic:
        nums.append(num_dic[char])

    # 입력된 문자가 연산자일 경우
    else:
        top = nums.pop()
        # 입력된 문자가 '+'일 경우
        if char == '+':
            nums[-1] += top
        # 입력된 문자가 '-'일 경우
        elif char == '-':
            nums[-1] -= top

        # 입력된 문자가 '*'일 경우
        elif char == '*':
            nums[-1] *= top
        # 입력된 문자가 '/'일 경우
        else:
            nums[-1] /= top

print(f'{nums[0]:.2f}')
