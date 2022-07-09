# 유형: 그리디
# 풀이방법:
# 로프가 한 개씩 증가할 때마다 최대 중량 W를 k*최소무게로 구하여 최대 중량의 최댓값을 구하기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
W = list(int(input()) for i in range(N))

W.sort(key=lambda x: -x) # 정렬

max_val = 0
for i in range(1, N+1):
    max_val = max(max_val, i*W[i-1])

print(max_val)