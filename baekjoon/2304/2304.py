import sys
sys.stdin = open('2304_input.txt', 'r')

N = int(input()) # 기둥의 개수
pillars = [0] * N # 기둥의 위치, 높이 리스트

# 기둥 입력 받기
for i in range(N):
    pillars[i] = tuple(map(int, input().split()))
# 위치를 기준으로 정렬
pillars.sort(key=lambda x: x[0])

# 최대값이 있는 인덱스를 찾는다.
max_idx = 0
for i in range(N):
    if pillars[i][1] >= pillars[max_idx][1]:
        max_idx = i

area = 0

# max 전까지 앞에서 부터 접근
cur_idx = 0 # 현재 기둥의 idx
for next_idx in range(1, max_idx + 1): # 다음 기둥의 idx
    cur_height = pillars[cur_idx][1]
    next_height = pillars[next_idx][1]

    if cur_height < next_height: # 현재 기둥이 작을 때
        area += cur_height * (pillars[next_idx][0] - pillars[cur_idx][0])
        cur_idx = next_idx

    elif cur_height ==  next_height: # 현재 기둥과 같을 때
        area += cur_height * (pillars[next_idx][0] - pillars[cur_idx][0])
        cur_idx = next_idx

# max 기둥 더해주기
area += pillars[max_idx][1]

# max 이후부터 뒤에서 부터 접근
cur_idx = N-1
for next_idx in range(N-2, max_idx-1, -1):
    cur_height = pillars[cur_idx][1]
    next_height = pillars[next_idx][1]
    if cur_height < next_height:  # 현재 기둥이 작을 때
        area += cur_height * (pillars[cur_idx][0] - pillars[next_idx][0])
        cur_idx = next_idx
print(area)
