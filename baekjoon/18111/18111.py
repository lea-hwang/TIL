import sys
sys.stdin = open('18111_input.txt', 'r')

N, M, B = map(int, input().split())
ground = [0] * 257

for _ in range(N):
    input_data = list(map(int, input().split()))
    for k in input_data:
        ground[k] += 1

for i in range(257):
    if ground[i]:
        min_idx = i
        break
for i in range(256, -1, -1):
    if ground[i]:
        max_idx = i
        break

time = 0
while max_idx - min_idx > 1:
    # 만약 수중에 블록이 있다면 min_idx에 블록을 채우고
    if B >= ground[min_idx] and ground[min_idx] <= ground[max_idx] * 2:
        ground[min_idx+1] += ground[min_idx]
        B -= ground[min_idx]
        time += ground[min_idx]
        min_idx += 1
    # 수중에 블록이 없다면 max_idx에서 블록을 제거한다.
    else:
        ground[max_idx-1] += ground[max_idx]
        time += 2 * ground[max_idx]
        B += ground[max_idx]
        max_idx -= 1

# 채워야하는 시간과 삭제하는 시간을 비교해서 둘 중 더 작은 시간을 택한다.
if min_idx != max_idx:
    if B >= ground[min_idx] and ground[min_idx] <= ground[max_idx] * 2:
        height = max_idx
        time += ground[min_idx]
    else:
        height = min_idx
        time += ground[max_idx] * 2
else:
    height = min_idx
print(time, height)

