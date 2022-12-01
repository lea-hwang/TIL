import sys
sys.stdin = open("input.txt")

chess_default = [1, 1, 2, 2, 2, 8]

chess_input = list(map(int,input().split()))

result = [0, 0, 0, 0, 0, 0]

for i in range(6):
  result[i] = chess_default[i] - chess_input[i]

print(*result)