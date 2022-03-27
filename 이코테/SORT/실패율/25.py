# 직관적으로 짠 코드, 시간초과 발생
# def solution(N, stages):
#     fail_stage = [0] * (N + 2)              # 해당 스테이지를 통과한 사람, 카운트 정렬
#     in_stage = [0] * (N + 2)                # 해당 스테이지에 참여한 사람, 누적
#     for stage in stages:
#         fail_stage[stage] += 1
#         for s in range(1, stage+1):
#             in_stage[s] += 1
#     P = [] * N
#     for i in range(1, N+1):
#         if in_stage[i]:                                                 # 제로 디비전 에러 해결
#             P.append([i, fail_stage[i]/in_stage[i]])                   # 실패율
#         else:
#             P.append([i, 0])
#
#     # 실패율 순서대로 정렬
#     P.sort(key=lambda p: -p[1])
#
#     answer = list(list(zip(*P))[0])
#
#     # print(stages)       # [2, 1, 2, 6, 2, 4, 3, 3]
#     # print(fail_stage)   # [0, 1, 3, 2, 1, 0, 1]
#     # print(in_stage)     # [0, 8, 7, 4, 2, 1, 1]
#     # print(P)            # [[3, 0.5], [4, 0.5], [2, 0.42857142857142855], [1, 0.125], [5, 0.0]]
#     return answer

def solution(N, stages):
    answer = []
    fail_P = [[i, 0] for i in range(N+2)]   # stage 번호, 실패율

    # stages 내림차순 정렬
    stages.sort(reverse=True) # [6, 4, 3, 3, 2, 2, 2, 1]

    # 포문 편하게 돌리기 위해 넣어줌(1단계를 위해)
    stages += [0]

    in_stage = [0]                                  # 해당 스테이지에 참여한 사람 저장
    pre_stage = 0
    # 큰 수부터 접근
    for i in range(len(stages)-1):
        # stages[i]: stage 번호
        if stages[i] != stages[i+1]:                    # 단계가 변하기 직전에
            in_stage.append(i + 1)                      # 참여한 사람 수
            fail_stage = in_stage[-1] - in_stage[-2]    # 참여한 사람 중에서 다음 단계로 넘어간 사람 제외시킴
            fail_P[stages[i]][1] = fail_stage/in_stage[-1]     # 실패율 저장

    fail_P.pop(0)   # 0단계 제거
    fail_P.pop()    # 올솔 제거

    # 실패율을 기준으로 내림차순 정렬
    fail_P.sort(key=lambda p: -p[1])

    # answer에 단계 저장
    for p in fail_P:
        answer.append(p[0])

    return answer




def main():
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))

main()