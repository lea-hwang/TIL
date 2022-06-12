import sys
sys.stdin = open('input.txt', 'r')

# 전투력이 높은 병사가 앞에 오도록 배치
# 특정 위치에 있는 병사 열외
# 남아있는 병사의 수 최대

N = int(input())
soldiers = list(map(int, input().split()))

s_cnt_list = [1] * N # 현재 병사보다 높은 병사 수(자기 자신 포함)를 저장할 리스트 (default는 자기 자신 1명)

max_val = 1

# 현재 병사보다 높은 병사 수 만큼 세고 + 1
for cur in range(N): # 현재 인덱스(각각의 병사)
    for prev in range(cur-1, -1, -1): # 이전 인덱스(각각의 병사의 이전 병사들)
        if soldiers[prev] > soldiers[cur] and s_cnt_list[prev] + 1 > s_cnt_list[cur]: # 이전 병사의 전투력이 현재 병사의 전투력보다 높을 때
            s_cnt_list[cur] = s_cnt_list[prev] + 1  # 이전 병사 cnt 에서 + 1
            max_val = max(max_val, s_cnt_list[cur]) # 최대 병사 수 갱신

print(N - max_val)
