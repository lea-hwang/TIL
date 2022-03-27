import sys
sys.stdin = open('10866_input.txt', 'r')

N = int(input())
deque = []
for _ in range(N):
    order = input()
    # order = sys.stdin.readline().strip()
    if 'push' in order:
        order, num = order.split()
        if order == "push_front":
            deque.insert(0, num)
        else:
            deque.append(num)
    else:
        if order == "pop_front":
            if len(deque):
                print(deque.pop(0))
            else:
                print(-1)
        elif order == "pop_back":
            if len(deque):
                print(deque.pop())
            else:
                print(-1)
        elif order == "size":
            print(len(deque))
        elif order == "empty":
            if len(deque):
                print(0)
            else:
                print(1)
        elif order == "front":
            if len(deque):
                print(deque[0])
            else:
                print(-1)
        else: # order == "back"
            if len((deque)):
                print(deque[-1])
            else:
                print(-1)