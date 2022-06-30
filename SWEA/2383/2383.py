import sys
sys.stdin = open('2383_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 사람 위치, 계단 위치 입력받기
    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                people.append((i, j))
            elif mat[i][j] >= 2:
                stairs.append((i, j))

    # 계단 * 사람 매트릭스 만들기
    distance = [[0] * len(people) for _ in range(2)]
    for i in range(2):
        for j in range((len(people))):
            distance[i][j] = abs(stairs[i][0] - people[j][0]) + abs(stairs[i][1] - people[j][1])

    # 가장



    print(f'#{tc} ')