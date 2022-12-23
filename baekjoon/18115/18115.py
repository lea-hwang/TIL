import sys
sys.stdin = open("input.txt")

from collections import deque

N = int(input())

cards = deque()
techniques = list(input().split())

for idx, technique in enumerate(techniques[::-1]):
    num = idx + 1
    if technique == "1":
        cards.appendleft(num)
    elif technique == "2":
        cards.insert(1, num)
    else:
        cards.append(num)

print(*cards)