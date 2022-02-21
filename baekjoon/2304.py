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
midx = 0
for i in range(N):
    if pillars[i][1] > pillars[midx][1]:
        midx = i

area = 0
for i in range(N):
    if i == midx: # 최댓값에 도달했을때 다음 최댓값을 찾는다
        pass
    else:
        pass

print(pillars)

