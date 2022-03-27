import sys
sys.stdin = open('1874_input.txt', 'r')


N = int(input())
stack = [0] * (N+1)
top = 0
i = 1
cnt = 0
result = []
while i < N + 1 or top > 0:
    k = int(input()) # 입력된 수
    cnt += 1
    if k > stack[top]:
        while k > stack[top]: # 가장 위에 있는 숫자가 k보다 작다면 push
            top += 1
            stack[top] = i
            result.append('+')
            i += 1      # 1씩 커짐
        top -= 1
        result.append('-')
    else:
        while k < stack[top]:
            top -= 1
            result.append('-')
        top -= 1
        result.append('-')
if cnt < N:
    while cnt < N:
        _ = input()
        cnt += 1
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])