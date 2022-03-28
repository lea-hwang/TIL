import sys
sys.stdin = open('20055_input.txt', 'r')


N, K = map(int, input().split()) # 컨베이어벨트의 길이, 내구도가 0인 칸의 개수(상한)
BELT_LENGTH = 2 * N
belt = list(map(int, input().split()))
robot = [0] * BELT_LENGTH


level = 0


def check_durability(): # 내구도의 개수가 K개를 넘지 않는지 체크한다.
    global K, belt
    if belt.count(0) >= K:
        return False
    else:
        return True


def move_robot(): # 이동할 수 있는 로봇을 이동시킨다
    global N
    # N-2에 로봇이 있고, N-1 칸의 내구성이 1이라면 로봇을 내린다
    if robot[N-2] and belt[N-1]:
        robot[N-2] = 0
        belt[N-1] -= 1

    # N-2부터 -N까지 거꾸로 접근하여 로봇을 이동시킨다.
    for i in range(N-2, -N, -1):
        # 현재 칸에 로봇이 있고, 이동하려는 칸에 로봇이 없고, 내구성이 1 이상일때 이동
        if robot[i-1] and not robot[i] and belt[i]:
            robot[i-1], robot[i] = 0, 1
            belt[i] -= 1


def turn_belt(): # 컨베이어 벨트를 회전시킨다
    global belt, robot, N
    belt = [belt[-1]] + belt[:-1]
    robot = [robot[-1]] + robot[:-1]
    # 로봇이 내리는 위치에 도달했다면 내린다
    if robot[N-1]:
        robot[N-1] = 0

def put_robot():
    global belt, robot
    if belt[0] and not robot[0]:
        robot[0] = 1
        belt[0] -= 1


# 실행
while check_durability():
    level += 1
    turn_belt()
    move_robot()
    put_robot()


print(level)





