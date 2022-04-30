import sys
sys.stdin = open('input.txt', 'r')

N = int(input())        # 남은 날짜
schedules = []          # 시작날짜, 끝 날짜, 수익

for start in range(1, N+1):
    time, money = map(int, input().split())
    schedules.append([start, start+time, money])     # [[1, 4, 10], [3, 4, 10], [4, 5, 15], [2, 7, 20], [5, 7, 15], [7, 9, 200], [6, 10, 40]]

schedules.sort(key=lambda x:(x[1], x[0]))            # 끝나는 날짜를 기준으로 정렬
dp = [0] * (N+2)

day = 1     # 현재 날짜
idx = 0     # 스케줄 index

# 각 날짜에 끝나는 스케줄 중, dp[시작 날짜] + 현재 수익의 값이 가장 높은 수익을 저장
while day < N+2 and idx < N:
    start, end, profit = schedules[idx]

    # 현재 날짜가 끝나는 날짜보다 빠르다면, 끝나는 날짜까지 dp의 값을 저장해둠
    while day < end and day < N+1:
        day += 1
        dp[day] = dp[day-1]

    # 만약 스케줄이 끝나는 날짜가 남을 일정을 벗어날 경우 break
    if end >= N+2:
        break

    # 저장된 값과 비교 후, 큰 값 저장
    cur_profit = dp[start] + profit
    dp[end] = max(dp[end], cur_profit)
    idx += 1


print(dp[N+1])
