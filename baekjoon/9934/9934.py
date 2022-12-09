import sys
sys.stdin = open("input.txt")

K = int(input())
turns = list(map(int, input().split()))

N = 2 ** K - 1
tree = [0] * (N+1)
turn = 0
def LVR(v):
    global turn
    # 왼쪽 자식노드를 방문한 적이 없다면
    if v*2 < N and not tree[v * 2]:
        LVR(v*2)
    tree[v] = turns[turn]
    turn += 1
    # 오른쪽 자식노드를 방문한 적이 없다면
    if v*2 < N and not tree[v * 2 + 1]:
        LVR(v*2+1)
LVR(1)

for i in range(0, K):
    print(*tree[2**i: 2**(i+1)])