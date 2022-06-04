# N*N 도시
# 빈 칸, 치킨집, 집

# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리 |r1-r2| + |c2-c2|
# 0: 빈칸, 1: 집, 2: 치킨집

# 문제 상황
# 도시에 있는 치킨집 중에서 최대 M 개를 선택, 치킨 거리의 최솟값

import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations

N, M = map(int, input().split()) # 도시의 크기, 치킨집의 개수(상한)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 도시 정보
INF = 987654321

# 치킨집의 위치와 집의 위치 따로 저장하기
chi_p = []
house_p = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chi_p.append((i, j))
        elif board[i][j] == 1:
            house_p.append((i, j))

# print(house_p)
# print(chi_p)

# 치킨집의 개수와 집의 개수
chi_cnt = len(chi_p)
house_cnt = len(house_p)

distance = [[0] * chi_cnt for _ in range(house_cnt)] # house_cnt * chi_cnt 크기의 거리 정보 matrix

# 치킨집과 모든 집 사이의 거리를 저장해두기
for h in range(house_cnt):
    for c in range(chi_cnt):
        distance[h][c] = abs(house_p[h][0] -  chi_p[c][0]) + abs(house_p[h][1] -  chi_p[c][1]) # |r1-r2| + |c2-c2|

# 치킨집 들 중 M개를 선택한 후 그 거리의 합을 구하고, 그 중 최소값을 구한다.
chi_M_selected = list(combinations(range(chi_cnt), M))

min_distance = INF

for chi_selected in chi_M_selected: # 선택된 치킨집을 기준으로 각 집에 대한 거리의 최솟값 찾고 그 합을 최솟값과 비교
    total = 0

    # 모든 집에 대해서 M개의 치킨집까지의 거리 중 최솟값 찾기
    for h in range(house_cnt):
        house_min_d = INF       # INF로 초기화
        for c in chi_selected:
            house_min_d = min(distance[h][c], house_min_d)

        total += house_min_d # 각 집에 대해서 최솟값 더해주기

    min_distance = min(total, min_distance) # 치킨거리 최솟값 갱신
# print(chi_M_selected)

print(min_distance)


