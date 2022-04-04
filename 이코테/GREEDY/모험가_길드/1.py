import sys
sys.stdin = open('input.txt', 'r')

N = int(input())  # 모험가 수
fear = list(map(int, input().split()))

fear.sort(reverse=True)

group = 0
i = 0
while i < N:
    group += 1
    i += fear[i]

print(group)
