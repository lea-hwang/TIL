import sys
sys.stdin = open('2110_input.txt', 'r')


def yes_I_can(distance): # 해당 길이로 공유기를 모두 설치할 수 있는지 여부 확인
    global C
    last_i = 0
    router = 0
    for i in range(1, len(houses)):
        bet_d = houses[i] - houses[last_i]  # last_i번째의 집 위치에서 i번째 집까지의 거리가
        if bet_d >= distance:               # distance 보다 크거나 같을 때 설치가능
            last_i = i                      # 마지막으로 설치된 공유기의 위치 갱신
            router += 1                     # 설치된 공유기의 개수 +1

    if router >= C-1:  # C-1개의 공유기를 모두 설치할 수 있을 때(첫번째는 이미 설치했다고 가정)
        return True
    else:
        return False


def binary_search():
    global left, right
    start, end = 0, right-left        # 이진탐색 하한, 상한

    max_d = 0                       # 최소 거리의 최댓값
    while start <= end:
        mid = (start + end) // 2
        if yes_I_can(mid):          # 공유기를 설치할 수 있을 때
            max_d = mid             # 최소 거리의 최댓값 갱신
            start = mid + 1
        else:                       # 공유기를 설치할 수 없을 때
            end = mid - 1
    return max_d


N, C = map(int, sys.stdin.readline().rstrip().split())                # 집의 개수, 공유기 개수
houses = [int(input()) for i in range(N)]       # 집의 좌표

houses.sort()                                   # 집의 위치 오름차순 정렬

left, right = houses[0], houses[-1]

print(binary_search())