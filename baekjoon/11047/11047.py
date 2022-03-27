import sys
sys.stdin = open('11047_input.txt', 'r')

N, K = map(int, input().split()) # 동전의 종류, 금액
coins = [int(input()) for _ in range(N)]

min_cnt = 0
for coin in coins[::-1]:
    if K // coin: # 현재 동전으로 낼 수 있다면
        min_cnt += K // coin # 현재 동전으로 낼 수 있는 만큼 내기
        K %= coin # 남은 금액 저장하기

print(min_cnt)
