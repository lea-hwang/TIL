# 유형: 그리디
# 풀이방법:
# 첫번째 스위치를 누른다고 가정했을 때, 그렇지 않았을 때 두가지 경우로 나누어서
# i-1번째의 전구가 켜져있는지 꺼져있는지 여부를 확인하고 스위치를 누를지 말지를 결정한다.
# 유의할점:
# 첫번째 스위치를 누른다고 가정 -> cnt 값을 +1 해주어야 함


import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
INF = int(1e9)

s1 = list(map(int, input())) # 현재 전구
s2 = s1.copy()
a = list(map(int, input()))

s2[0] = not s2[0] # 첫번째 스위치를 누른다고 가정
s2[1] = not s2[1]

def solution(s, cnt):
    for i in range(1, N):
        if s[i-1] != a[i-1]: # i-1번째 전구가 다를 경우 스위치 누르기
            cnt += 1
            s[i-1] = not s[i-1]
            s[i] = not s[i]
            if i+1 < N:
                s[i+1] = not s[i+1]
    if s[N-1] == a[N-1]:
        return cnt
    return INF


answer = min(solution(s1, 0), solution(s2, 1))

if answer != INF:
    print(answer)
else:
    print(-1)