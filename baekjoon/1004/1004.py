import sys
sys.stdin = open("input.txt")

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

T = int(input())

for test in range(T):
    # 출발점, 도착점
    x1, y1, x2, y2 = map(int, input().split())

    # 행성 수
    N = int(input())

    planets = [0] * N

    for i in range(N):
        # 각 행성의 위치 & 반지름
        cx, cy, r = map(int, input().split())

        # 각 행성에 대해 거리를 구한다.
        D1 = get_distance(cx, cy, x1, y1)
        D2 = get_distance(cx, cy, x2, y2)

        if D1 < r:
            planets[i] += 1
        if D2 < r:
            planets[i] += 2
    count = 0

    for k in planets:
        if k == 1 or k == 2:
            count += 1

    print(count)
