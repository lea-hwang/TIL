import sys

sys.stdin = open("input.txt")

N, M = map(int, sys.stdin.readline().rstrip().split())
levels = []

for i in range(N):
  tmp = sys.stdin.readline().rstrip().split()
  tmp = [tmp[0], int(tmp[1])]
  # 만약 겹치는 레벨이 있다면 제외
  if levels and levels[-1][1] == tmp[1]:
    continue
  else:
    levels.append(tmp)

levels.sort(key=lambda x: x[1])


def binary_search(start, end, value):
  global levels
  
  while start < end:
    mid = (start + end) // 2
    if levels[mid][1] < value:
      start = mid + 1
    else:
      end = mid
  print(levels[start][0])
total_length = len(levels) -1 
for i in range(M):
  fight_ability = int(sys.stdin.readline().rstrip())
  binary_search(0, total_length, fight_ability)