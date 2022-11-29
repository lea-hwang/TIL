# 유형: 그리디
# 풀이방법:
# 순서대로 나열 후 음수와 양수 파트를 분리한다.
# 그 이후 가장 먼 책을 제일 마지막에 꽂는다(한번만 이동하기 위함)
# 나머지 책들 중, 음수는 작은 수부터 양수는 큰 수부터(절대값이 높은 책부터) 먼저 꽂는다.
# 유의할 점:
# 양수, 음수 파트 둘 중 하나라 없는 경우를 고려해야 함.

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
books = list(map(int, input().split()))

books.sort() # 위치 순으로 정리

# 양수, 음수 파트 분리
pos = []
neg = books # 양수 파트가 아예 없는 경우를 대비
for i in range(N):
    if books[i] > 0:
        pos = books[i:]
        neg = books[:i]
        break

total = 0

# 가장 먼 책 마지막에 꽂기
# 왼쪽만 있는 경우
if len(pos) == 0:
    total += -(neg[0])
    neg = neg[M:]
# 오른쪽만 있는 경우
elif len(neg) == 0:
    total += pos[-1]
    pos = pos[:len(pos) - M]
# 둘 다 있는 경우
else:
    if abs(neg[0]) > abs(pos[-1]): # 왼쪽을 먼저 꽂을때
        total += -(neg[0])
        neg = neg[M:]
    else:
        total += pos[-1]
        pos = pos[:len(pos) - M]

total += 2 * (-sum(neg[0::M]) + sum(pos[::-M]))

print(total)