

import sys
sys.stdin = open("1874_input.txt")

input = sys.stdin.readline

signs = []
n = int(input())
stack = [0]
top = 0
for t in range(n):
    k = int(input())
    # 스택의 가장 위에 있는 숫자가 방금 입력된 숫자보다 작다면 -> 더 넣어주어야 함.
    # 출력할 숫자가 제일 마지막 숫자보다 큰 경우 -> break(턴종료)
    if stack[-1] < k:
        if top > k:
            print("NO")
            break
        while top < k:
            top += 1
            stack.append(top)
            signs.append("+")
        # 마지막에 숫자를 빼주어야함
        stack.pop()
        signs.append("-")
    elif stack[-1] == k:
        stack.pop()
        signs.append("-")
    # 출력할 숫자가 제일 마지막 숫자보다 작은 경우
    else:
        print("NO")
        break
else:
    for sign in signs:
        print(sign)