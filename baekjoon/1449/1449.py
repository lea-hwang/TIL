# 유형: 그리디
# 풀이방법:
# 시작점에 일단 붙이고, 이후 지점들에서 테이프를 붙이지 못할때 새로운 테이프를 붙인다

import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split()) # 테이프의 개수, 테이프의 길이
H = list(map(int, input().split()))

H.sort()

start = H[0]
cnt = 1
for i in range(N):
    # 테이프 내에 있을 경우
    if H[i] < start + L:
        continue
    start = H[i]
    cnt += 1

print(cnt)



