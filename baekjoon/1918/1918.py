import sys
sys.stdin = open('1918_input.txt', 'r')

formula = input()
N = len(formula)

operator = [] # 연산자를 저장할 스택
pro = ''   # 후위 표기식을 저장할 스택

for char in formula:
    # 받은 문자가 '('일 경우
    if char == '(':
        operator.append(char)

    # 받은 문자가 ')'일 경우
    elif char == ')':
        while operator:
            if operator[-1] == '(': # 만약 '('가 가장 위에 쌓여있을 경우 pop하고 break
                operator.pop()
                break
            pro += operator.pop() # 후위 표기식에 추가

    # 받은 문자가 '+', '-'일 경우
    elif char == '+' or char == '-':
        while operator:
            if operator[-1] == '(': # 만약 '('가 가장 위에 쌓여있을 경우 break
                break
            pro += operator.pop() # 후위 표기식에 추가
        operator.append(char) # 연산자 스택에 추가

    # 받은 문자가 '*', '/'일 경우
    elif char == '*' or char == '/':
        while operator:
            if operator[-1] in '+-(': # 만약 '+', '-', '('가 가장 위에 쌓여있을 경우 break
                break
            pro += operator.pop() # 후위 표기식에 추가
        operator.append(char) # 연산자 스택에 추가

    # 받은 문자가 숫자일 경우
    else: # char in 'ABCDE..'
        pro += char # 후위 표기식에 추가

# 스택에 연산자가 남아있을 경우
while operator:
    pro += operator.pop()

print(pro)