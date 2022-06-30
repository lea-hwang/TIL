import sys
sys.stdin = open('4013_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    K = int(input()) # 자석 회전 횟수
    magnets = [list(map(int, input().split())) for _ in range(4)] # 자석 정보, N이 0 S가 1

    ptr_0 = [0, 0, 0, 0] # 처음 톱니바퀴가 가리키고 있는 위치

    for i in range(K): # K번 만큼 회전
        n, d = map(int, input().split()) # 회전시키려는 자석의 번호, 회전방향(1일 경우 시계방향, -1일 경우 반시계방향)
        turn = [0, 0, 0, 0]

        n -= 1 # 자석번호 -1

        # 해당 톱니바퀴 돌리기
        turn[n] = -d
        # 해당 톱니바퀴를 기준으로 왼쪽 확인
        for mag in range(n-1, -1, -1):
            left_ptr = (ptr_0[mag] + 2) % 8
            right_ptr = ptr_0[mag+1] - 2
            left = magnets[mag][left_ptr] # 왼쪽 톱니바퀴 자성
            right = magnets[mag+1][right_ptr] # 오른쪽 톱니바퀴 자성
            if left != right: # 극이 반대라면 돌려야할 바퀴 표시
                turn[mag] = d if (n - mag) % 2 else -d
            else:
                break

        # 해당 톱니바퀴를 기준으로 오른쪽 확인
        for mag in range(n+1, 4):
            left_ptr = (ptr_0[mag - 1] + 2) % 8
            right_ptr = ptr_0[mag] - 2
            left = magnets[mag - 1][left_ptr]  # 왼쪽 톱니바퀴 자성
            right = magnets[mag][right_ptr]  # 오른쪽 톱니바퀴 자성
            if left != right:  # 극이 반대라면 돌려야할 바퀴 표시
                turn[mag] = d if (mag - n) % 2 else -d
            else:
                break

        for mag in range(4):
            ptr_0[mag] = (ptr_0[mag] + turn[mag]) % 8

    score = 0
    for mag in range(4):
        score += magnets[mag][ptr_0[mag]] * 2 ** mag
    print(f'#{tc} {score}')