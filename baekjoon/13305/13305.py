# 유형: 그리디
# 풀이방법:
# 더 낮은 주유비를 지불할 수 있을때 그때 더 낮은 유류비를 지불한다.


import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input()) # 도시의 수
D = list(map(int, input().split())) # 거리
P = list(map(int, input().split())) # 주유비

total = 0
oil = P[0]

for i in range(N-1):
    oil = min(oil, P[i])
    total += oil * D[i]

print(total)

