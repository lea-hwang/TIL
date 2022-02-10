import sys
sys.stdin = open('2304.txt', 'r')

# 기둥의 개수
N = int(input())
# 기둥의 높이 리스트
pillars = []
# 기둥 입력 받기
for _ in range(N):
    pillars.append(tuple(map(int, input().split())))
# 기둥의 위치를 기준으로 정렬
pillars.sort(key=lambda x: x[0])
# 오른쪽에 있는 기둥이 나보다 클 때, pop
i = 1
while i < N:
    for j in range(i, N):
        if pillars[i][1] < pillars[j][1]:
            pillars.pop(i)
            N -= 1
            break
    else:
        i += 1
print(pillars)
# 전체 면적, 첫번째 기둥으로 초기화
area = pillars[0][1]
for j in range(1, N):
    # 왼쪽 기둥이 더 낮을 때
    if pillars[j][1] > pillars[j - 1][1]:
        # 왼쪽 기둥과 오른쪽 기둥 사이
        area += pillars[j - 1][1] * (pillars[j][0] - pillars[j - 1][0] - 1)
        # 오른쪽 기둥
        area += pillars[j][1]
    # 왼쪽 기둥이 더 높을 때
    else:
        area += pillars[j][1] * (pillars[j][0] - pillars[j - 1][0])
print(area)