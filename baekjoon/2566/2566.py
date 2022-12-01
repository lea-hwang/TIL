import sys
sys.stdin = open("./input.txt")

max_val = 0
position = (0, 0)
for i in range(9):
  line = list(map(int, input().split()))
  for j in range(9):
    if max_val <= line[j]:
      max_val =  line[j]
      position = (i+1, j+1)

print(max_val)
print(*position)