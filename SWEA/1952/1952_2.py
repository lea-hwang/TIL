# 풀이시간: 33분
# 시간: 5초
# 메모리: 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내
# 알고리즘: DP

# 풀이 방법
## DP를 이용하여 이전 달에서 이용권을 썼을 때의 최소비용을 구한다.
## 라고 했으나 모든 경우의 비용을 구해야한다는 사실을 깨달음.

# 함수 설계
## solution: 4가지 이용권을 모두 사용하는 방식으로 계산

# 느낀 점


import sys
sys.stdin = open('1952_input.txt', 'r')

T = int(input())

def solution(month, payment):
    global min_val
    # 종료조건
    if month >= 12:
        min_val = min(min_val, payment)
        return

    # 1일 이용권
    solution(month + 1, payment + schedules[month] * fees[0])
    # 1달 이용권
    solution(month + 1, payment + fees[1])
    # 3달 이용권
    solution(month + 3, payment + fees[2])



for tc in range(1, T+1):
    fees = list(map(int, input().split()))
    schedules = list(map(int, input().split()))
    min_val = fees[3] # 1년 이용권으로 금액 초기화

    solution(0, 0)

    print(f'#{tc} {min_val}')