import sys

sys.stdin = open('2116_input.txt', 'r')


def faced_number(dice, N): # 맞은 편에 위치한 숫자 return
    idx = dice.index(N)
    if idx == 0:
        return dice[5]
    elif idx == 1:
        return dice[3]
    elif idx == 2:
        return dice[4]
    elif idx == 3:
        return dice[1]
    elif idx == 4:
        return dice[2]
    else: # idx == 5
        return dice[0]

def highest_side(dice, N):
    nums = {1, 2, 3, 4, 5, 6}
    nums -= {N}
    nums -= {faced_number(dice, N)}
    return max(nums)

N = int(input())  # 주사위 수
dices = [list(map(int, input().split())) for i in range(N)]  # 주사위들
max_sides = 0

for num in range(1, 7):
    top_bottom = [num] # 각 주사위의 위아래 숫자를 넣을 것
    sides = [] # 각 주사위의 옆면 중 최댓값만 모아서 넣을 것
    for dice in dices: # 각 주사위 마다
        sides += [highest_side(dice, top_bottom[-1])] # 윗면을 기준으로 옆면을 찾아 넣는다(그 중 최댓값)
        top_bottom += [faced_number(dice, top_bottom[-1])] # 윗면을 기준으로 아랫면을 찾아 넣는다
    sum_sides = sum(sides) # 옆면 모두 더하기
    if max_sides < sum_sides:
        max_sides = sum_sides
print(max_sides)
