import sys
#sys.stdin = open('10845_input.txt', 'r')

N = int(input())
que = []

for i in range(N):
    order = sys.stdin.readline().strip()
    if 'push' in order:
        push_num = int(order.split()[1])
        que.append(push_num)
    else:
        if order == "pop":
            if len(que):
                print(que.pop(0))
            else:
                print(-1)
        elif order == "size":
            print(len(que))
        elif order == "empty":
            if len(que):
                print(0)
            else:
                print(1)
        elif order == "front":
            if len(que):
                print(que[0])
            else:
                print(-1)
        else: # order == "back"
            if len((que)):
                print(que[-1])
            else:
                print(-1)