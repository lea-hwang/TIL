import sys
sys.stdin = open('18111_input.txt', 'r')

N, M, B = map(int, input().split())
ground = []

for _ in range(N):
    ground += list(map(int, input().split()))

max_ground = max(ground)
min_ground = min(ground)

time = [0] * (max_ground - min_ground + 1)

ground.sort(reverse=True) # 블록 제거를 먼저할 수 있도록 유도(블록 인벤토리 저장)


# min ~ max 높이마다 얼마만큼의 시간이 걸리는지 체크
for i in range(max_ground - min_ground + 1):
    block = B
    height = min_ground + i
    for g in ground:
        if height > g: # 블록 제거
            block += height - g
            time[i] += 2 * (height - g)
        else:  # 블록 생성
            if block:
                block -= g - height
                time[i] += (g - height)
            else:
                time[i] = 256 * M * N * 2
                break


print(time)
min_time = min(time)
print(min_time, min_ground + time.index(min_time))