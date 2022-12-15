import sys
sys.stdin = open("1918_input.txt")

# 식을 입력받기
infix = input()

profix = []
signs = []
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}     # stack 쌓는 우선순위
for letter in infix:
    if letter == '(':
        signs.append(letter)
    elif letter == ')':
        # (가 나올 때까지 기호 꺼내기
        while True:
            top = signs.pop()
            if top == '(':
                break
            else:
                profix.append(top)
    elif letter in '+-*/':
        # 스택의 마지막 기호보다 우선순위가 낮을 때, 쌓기
        # 스택의 마지막 기호보다 우선순위가 높거나 같을 때, 낮을 때까지 빼내기
        # 스택이 비어있다면 바로 넣기
        while len(signs):
            top = signs[-1]
            if priority[top] < priority[letter]:
                break
            else:
                profix.append(signs.pop())
        signs.append(letter)
    # 문자일 때,
    else:
        profix.append(letter)
# 남은 기호 붙이기
profix.extend(signs[::-1])

# 결과
print(''.join(profix))