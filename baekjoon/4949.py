import sys
sys.stdin = open('4949_input.txt', 'r')

while True:
    sentence = input()

    if sentence == '.': #.이 입력되면 탈출
        break

    stack = [] # 괄호를 담을 리스트
    pair = 'yes'
    for letter in sentence:
        if letter == '(' or letter == '[':
            stack.append(letter)
        elif letter == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                pair = 'no'
                break
        elif letter == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                pair = 'no'
                break
    if len(stack) > 0:
        pair = 'no'

    print(pair)
