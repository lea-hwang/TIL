import sys
sys.stdin = open("1966_input.txt")
# 60분

# 우선순위 9부터 1까지 차례대로 내려가면서, 각 위치를 리스트에 담는다.

T = int(input())
def find_num(idxs, find_num):
    # idxs: [[], [0, 1, 3, 4, 5], [], [], [], [], [], [], [], [2]]
    turn = 0 # 순서
    end_idx = 0 # 이전 우선순위에서 가장 마지막이 되는 숫자
    for idx_list in idxs[::-1]: # 9에서 1까지 내려오면서, 해당 숫자를 찾으면 순서 출력
        if len(idx_list):
            # 이전 우선순위에 이어서 진행하기 위해 위치 찾기
            end_next_i = 0
            for i, idx in enumerate(idx_list):
                if idx >= end_idx:
                    end_next_i = i
                    break
            if find_num not in idx_list: # 찾는 숫자가 없다면 해당 길이만 더해주기
                turn += len(idx_list)
                end_idx = idx_list[end_next_i-1]
            else:
                # 새로운 리스트 만들기
                idx_list = [] + idx_list[end_next_i:] + idx_list[:end_next_i]
                
                # 찾는 숫자의 위치 파악
                find_idx = idx_list.index(find_num)
                return turn + find_idx + 1

for _ in range(T):
    N, M = map(int, input().split()) # 문서의 개수, 궁금한 문서
    importances = list(map(int, input().split()))
    idxs = [[] for i in range(10)]
    
    for idx, importance in enumerate(importances):
        idxs[importance].append(idx)
    

    print(find_num(idxs, M)) 