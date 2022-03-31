import sys
sys.stdin = open('2110_input.txt', 'r')


N, C = map(int, input().split())                    # 집의 개수, 공유기의 개수
houses = [int(input()) for _ in range(N)]           # 집의 좌표

# C개의 공유기를 N개의 집에 설치하여, 가장 인접한 두 공유기 사이의 거리를 최대로 하기.

# 1 2 4 8 9
# 제일 왼쪽과 제일 오른쪽에 설치.
# 남은 공유기를 가운데...에 설치?

# 1 2 3 4 5 9 10
def binary_search(start, end, target):
    # 현재 start와 end를 기준으로 가장 중앙에 가까운 수를 찾는다.
    # 해당 숫자를 따로 저장한다.
    # 만약 