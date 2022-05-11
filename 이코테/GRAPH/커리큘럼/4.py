# 위상정렬
# 1. 진입차수가 0인 노드를 찾는다.
# 2. 해당 노드와 연결된 노드를 queue에 저장한다.
# 3.

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

N = int(input())                # 강의수
pre_lec = [0] * N               # 선이수 과목 수(진입차수)
time = [0] * N                  # 강의 시간
graph = [[] for i in range(N)]  # 각 강의의 선이수 과목
total_time = [0] * N            # 선이수 과목을 포함한 총 수강 시간


# 각 강의의 강의 시간, 각 강의를 듣기 위해 먼저들어야하는 강의번호
for i in range(N):
    input_data = sys.stdin.readline().split()
    time[i] = input_data[0]
    # 각 강의의 선이수 과목 저장
    for lec in input_data[1:-1]:
        graph[i].append(lec)
        # 진입차수 += 1
        pre_lec[i] += 1

queue = deque()

for i in range(N):
    # 선이수 과목이 없는 과목 찾기
    if pre_lec[i] == 0:
        queue.append(i)

while queue:
    # 현재 노드
    v = queue.popleft()
    # 현재 노드와 연결된 모든 노드를 queue에 넣어주기
    for nxt in graph[v]: # nxt는 다음 이수 과목
        # 더 오래 걸리는 시간으로 바꾸기
        total_time[nxt] = max(total_time[nxt], total_time[v] + time[nxt])
        pre_lec[nxt] -= 1


