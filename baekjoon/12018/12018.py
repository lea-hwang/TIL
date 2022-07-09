# 유형: 그리디
# 풀이방법
# 각 과목당 필요한 마일리지를 구해 현재 마일리지로 들을 수 있는 과목수를 구한다.

import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n, m = map(int, input().split())  # 과목 수, 마일리지
min_M = [0] * n

for i in range(n):
    P, L = map(int, input().split())  # 각 과목에 신청한 사람 수, 과목의 수강인원
    M = list(map(int, input().split()))  # 넣은 마일리지
    if P >= L:
        M.sort()
        min_M[i] = M[P - L]
    else:
        min_M[i] = 1


min_M.sort()  # 오름차순 정렬

total = 0
cnt = 0
for i in range(n):
    if total + min_M[i] > m:
        break
    total += min_M[i]
    cnt += 1

print(cnt)

