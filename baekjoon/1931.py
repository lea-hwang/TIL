import sys
sys.stdin = open('1931_input.txt', 'r')

N = int(input()) # 회의의 수
meetings = [list(map(int, input().split())) for _ in range(N)]
visit = [0] * N
top = 0
def binary_tree(i, N):
    global top
    if top < sum(visit):
        top = sum(visit)
    if i == N:
        return

    start, end = meetings[i][0], meetings[i][1]
    for j in range(i):
        if visit[j]: # 이전 회의가 잡혀있을 때
            if not (start >= meetings[j][1] or end <= meetings[j][0]): # 이전 회의와 겹치는 경우
                break
    else:
        visit[i] = 1
        binary_tree(i + 1, N)
    visit[i] = 0
    binary_tree(i + 1, N)


binary_tree(0, N)
print(top)
# 각 회의를 진행 여부를 확인.
# 먼저, 현재 회의 진행가능한지 확인.
# 회의가 가능하면 다음 회의 가능 여부 확인
# 회의가 불가능 하면 리턴

meets = [list(map(int, input().split())) for _ in range(N)]

def binary_tree(N):
    top = 0
    stack = [0]
    while True:
        curr = stack.pop()
        


    if top < sum(visit):
        top = sum(visit)
    if i == N:
        return

    start, end = meetings[i][0], meetings[i][1]
    for j in range(i):
        if visit[j]: # 이전 회의가 잡혀있을 때
            if not (start >= meetings[j][1] or end <= meetings[j][0]): # 이전 회의와 겹치는 경우
                break
    else:
        visit[i] = 1
        binary_tree(i + 1, N)
    visit[i] = 0
    binary_tree(i + 1, N)


