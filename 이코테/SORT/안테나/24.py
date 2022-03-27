import sys
sys.stdin = open('24_input.txt', 'r')

N = int(input())                                # 집의 수
houses = list(map(int, input().split()))        # 집의 위치 정보

# 집 위치 정렬
houses.sort()

# # 제일 왼쪽 집에서부터 오른쪽 집까지 각각의 위치에서 거리의 합을 구하여 최소가 되는 지점을 찾는다.
# min_distance = houses[-1] * N
# min_house = houses[-1]
# for x in range(1, houses[-1]+1):
#     distance = 0
#     for house in houses:
#         distance += abs(x-house)
#     if min_distance > distance: # 현재 거리의 합이 더 작다면 갱신
#         min_distance = distance
#         min_house = x
#
# print(min_house)
# -> 시간 초과

# 중앙값을 찾는다.
if len(houses) % 2:                 # 홀수 개의 집이 있다
    print(houses[len(houses)//2])
else:                               # 짝수 개의 집이 있다
    # 가운데에 위치한 두개의 집의 중 왼쪽에 있는집
    print(houses[len(houses)//2-1])

