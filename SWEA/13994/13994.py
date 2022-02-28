import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bus_num = int(input())
    buses = [list(map(int, input().split())) for i in range(bus_num)]
    lines = [0]*1001
    for bus in buses:
        # 일반 버스
        if bus[0] == 1:
            for i in range(bus[1], bus[2]+1):
                lines[i] += 1
        # 급행 버스
        elif bus[0] == 2:
            lines[bus[2]] += 1
            for i in range(bus[1], bus[2], 2):
                lines[i] += 1
        # 광역 버스
        else:
            lines[bus[1]] += 1
            lines[bus[2]] += 1
            # 시작점이 홀수일 때
            if bus[1] % 2:
                for i in range(bus[1] + 1, bus[2]):
                    if not (i % 3) and i % 10:
                        lines[i] += 1
            else: # 시작점이 짝수일 때
                for i in range(bus[1] + 1, bus[2]):
                    if not (i % 4):
                        lines[i] += 1

    print(f'#{tc} {max(lines)}')