import sys
sys.stdin = open('input.txt', 'r')

N = int(input())    # 남은 날짜
schedule = []       # 시작날짜, 끝 날짜, 수익

for start in range(1, N+1):
    time, money = map(int, input().split())
    schedule.append([start, start+time, money])

schedule.sort(key=lambda x:(x[1], x[0]))
print(schedule)
dp = [0] * (N+1)
# 최대 수익 구하기
# 가정
#.. 새로운 아이디어 필요...
