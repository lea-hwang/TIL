import sys
sys.stdin = open('1966_input.txt', 'r')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # 문서의 개수, 궁금한 문서
    if N == 1:
        priority = int(input())
        print(1)
    else:
        priority = list(map(int, input().split()))
        front = 0

        found = False
        order = 0
        while not found:
            top_priority = max(priority)
            while True:
                if priority[front] == top_priority:
                    order += 1
                    if front == M:
                        found = True
                        break
                    priority[front] = 0
                    front = (front + 1) % N
                    break
                front = (front + 1) % N
        print(order)
