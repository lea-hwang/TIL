import sys

sys.stdin = open('10773_input.txt', 'r')

K = int(input())
num_stack = [0] * K
top = -1
for i in range(K):
    cur = int(input())
    if cur == 0:
        top -= 1
    else:
        top += 1
        num_stack[top] = cur
print(sum(num_stack[:top+1]))