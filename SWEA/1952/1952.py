import sys
sys.stdin = open('1952_input.txt', 'r')


def dfs(month, payment):
    global min_val
    if payment > min_val:
        return
    if month >= 12:
        min_val = payment
        return
    # 1일 이용권
    dfs(month+1, payment + fee[0] * frequency[month])
    # 1달 이용권
    dfs(month+1, payment + fee[1])
    # 3달 이용권
    dfs(month+3, payment + fee[2])




T = int(input())
for tc in range(1, T+1):
    fee = list(map(int, input().split())) # 1일, 1달, 3달, 1년
    frequency = list(map(int, input().split()))
    min_val = fee[3]    # 1년 이용권으로 초깃값 설정
    dfs(0, 0)

    print(f'#{tc} {min_val}')
