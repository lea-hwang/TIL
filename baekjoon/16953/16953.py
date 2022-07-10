# 유형: 그리디
# 풀이방법:
# 모든 경우의 수 헤아리기. backtracking -> B를 넘어갈 경우 break

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
answer = -1

queue = deque([(A, 1)])
while queue:
    num, times = queue.popleft()
    num1 = num * 2
    num2 = num * 10 + 1
    if num1 == B or num2 == B:
        answer = times + 1
        break
    if num1 < B:
        queue.append((num1, times+1))
    if num2 < B:
        queue.append((num2, times+1))

print(answer)