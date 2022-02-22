C, R = map(int, input().split()) # 공연장 크기 C:가로 R:세로
K = int(input()) # 대기번호
ud_lr = 0 # 현재 어느 변에 있는지, 
# 0: 상, 
# 1: 우, 
# 2: 하, 
# 3: 좌  # 상하는 짝수 # 좌우는 홀수
position = [1, 0]# 현재 위치

C -= 1

if K <= C * R:
    while K:
        if ud_lr % 2: # 좌우
            if K > C: # 다음 라인으로 이동
                if ud_lr == 3: # 좌
                    position[0] -= C
                else: # 우
                    position[0] += C
                K -= C
                C -= 1
            else:
                break
        else: # 상하
            if K > R: # 다음 라인으로 이동
                if ud_lr == 0: # 상
                    position[1] += R
                else: # 하
                    position[1] -= R
                K -= R
                R -= 1
            else:
                break
        ud_lr = (ud_lr + 1) % 4
    
    if ud_lr == 0: # 상
        position[1] += K
    elif ud_lr == 1: # 우
        position[0] += K
    elif ud_lr == 2: # 하
        position[1] -= K
    else: # 좌
        position[0] -= K
    print(*position)
else:
    print(0)