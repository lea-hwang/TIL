import sys
sys.stdin = open('17626_input.txt', 'r')

N = int(input())
limit = int(N ** (1/2))

# 제곱근 여부 확인
if N ** (1/2) % 1 == 0:
    print(1)
    sys.exit(0)

three = False
for i in range(1, limit + 1):
    a = i**2
    for j in range(1, limit + 1):
        b = j**2
        if a + b == N: # 2개를 찾았을때
            print(2)
            sys.exit(0)
        elif a + b > N: break
        if (N - a - b) ** (1/2) % 1 == 0:
            three = True
if three:
    print(3)
else:
    print(4)