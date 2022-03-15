import sys
sys.stdin = open('5648_input.txt', 'r')

d_rc = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 상하좌우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [[0] * 2001 for _ in range(2001)]
    for i in range(N):
        atom = list(map(int, input().split())) # x 위치, y 위치, 이동방향, 보유에너지
        grid[atom[0]][atom[1]] = [atom[2], atom[3]] # 이동방향, 보유에너지 저장
    energy = 0
    # 각 atom에 대해, 한 원자를 기준으로 한칸씩 이동하며, 다른 원자와 충돌 가능성이 있는지 살핀다.
    # 원자의 원래 위치에서 현재 위치까지의 거리를 구하고, 그 거리만큼 다른 방향의 원자 여부를 살핀다.
    # 만약 만나는 원자가 있을 경우

    print(f'#{tc} {energy}')