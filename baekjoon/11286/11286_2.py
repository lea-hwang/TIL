# 메모리: 39760KB 시간: 152ms
# 풀이시간: 10분

import sys
import heapq
sys.stdin = open("input.txt")

heap = []

N = int(input())

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        heapq.heappush(heap, (abs(n), n))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)