# n * n 크기의 정사각 격자
# [x, y, a, b]
# [가로, 세로, 설치할 구조물, 설치삭제여부]
# a: 0은 기둥 1은 보
# b: 0은 삭제 1은 설치

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 함
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함


def solution(n, build_frame):
    answer = []
    # 기둥의 위치와 보의 위치를 저장

    for x, y, a, b in build_frame:
        if b == 1: # 설치
            if a == 0: # 기둥
                # 바닥 위에 있거나
                if y == 0:
                    answer.append((x, y, 0))
                # 보의 한쪽 끝 부분 위에 있거나
                elif (x, y, 1) in answer or (x-1, y, 1) in answer:
                    answer.append((x, y, 0))
                # 다른 기둥 위에 있거나
                elif (x, y-1, 0) in answer:
                    answer.append((x, y, 0))
            else: # 보
                # 한쪽 끝 부분이 기둥 위에 있거나
                if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer:
                    answer.append((x, y, 1))
                # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
                elif (x-1, y, 1) in answer or (x+1, y, 1) in answer:
                    answer.append((x, y, 1))
        else: # 삭제
            pass
    answer.sort()
    return answer



print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))