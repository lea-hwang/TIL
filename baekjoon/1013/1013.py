import sys
sys.stdin = open('1013_input.txt', 'r')

def check_sign(sign): # 해당 사인이 올바른 패턴인지 확인
    # 현재 인덱스, sign의 전체 길이
    idx = 0
    N = len(sign)
    while idx < N:
        if sign[idx]: # 현재 인덱스에 해당하는 숫자가 1인 경우
            k = 0
            while ((idx + 1 + k) < N) and (sign[idx + 1 + k] == 0):
                k += 1
            if k < 2:
                return False
            else:
                idx += k + 2
        else: # 0인 경우
            if (idx + 1 < N) and sign[idx+1]: # 0 다음 숫자가 1 인경우
                idx += 2
            else:
                return False
    return True

T = int(input())
for _ in range(T):
    sign = list(map(int, input()))

    if check_sign(sign):
        print('YES')
    else:
        print('NO')