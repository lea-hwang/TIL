import sys
sys.stdin = open('input.txt', 'r')

import heapq


N = int(input())
heap = []
len_heap = 0
for i in range(N):
    num = int(input())
    if num:
        heapq.heappush(heap, num)
        len_heap += 1
    else:
        if len_heap > 0:
            print(heapq.heappop(heap))
            len_heap -= 1
        else:
            print(0)