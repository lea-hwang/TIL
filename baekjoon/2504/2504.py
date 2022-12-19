import sys
sys.stdin = open("input.txt")

line = input()
stack = []

# (, [ 일 경우, stack에 쌓기
# ) 일 경우, (가 나올 때까지 점수 계산하기
def get_score(line):
    for sign in line:
        score = 0
        if sign in '([':
            stack.append(sign)
        elif sign == ')':
            while stack:
                top = stack.pop()
                if isinstance(top, int): # 숫자가 들어있을 경우
                    score += top
                elif top == '(':
                    if not score: score = 1 # 만약 제일 안쪽 괄호일 경우,
                    stack.append(score * 2)
                    break
                else: # 잘못된 괄호
                    return False
        else: # sign == ']'
            while stack:
                top = stack.pop()
                if isinstance(top, int): # 숫자가 들어있을 경우
                    score += top
                elif top == '[':
                    if not score: score = 1 # 만약 제일 안쪽 괄호일 경우,
                    stack.append(score * 3)
                    break
                else: # 잘못된 괄호
                    return False
        if not stack: # stack이 비어있다면 잘못됨.
            return False
    # 만약 stack 속 모든 값이 숫자가 아닐 경우,
    for num in stack:
        if not isinstance(num, int):
            return False
    return True

if get_score(line):
    print(sum(stack))
else:
    print(0)


# 33분