# hanoi(1): 첫번째 원판을 세번째 장대로 옮긴다
# hannoi(2) : 이전 판들을 전부 두번째 장대로 옮기고, 두번째 원판을 3번째로 옮기고, 나머지를 다시 3번째로 옮긴다.

#hannoi(n, d, c) n 원판의 개수, d 목표 장대, c 현재 장대
# 만약 현재 원판의 개수가 홀수인지 짝수인지 확인
# 결국 마지막에 제일 마지막 판을 3번째에 둬야함.
#

# n의 경우
#           홀수인 경우
#           hannoi(1, 3) -> hannoi(2, 2) -> hannoi(3, 3) -> hannoi(4, 2) -> ... -> hannoi(n, 3)
#           짝수인 경우
#           hannoi(1, 2) -> hannoi(2, 3), -> hannoi(3, 2) -> hannoi(4, 3) -> ... -> hannoi(n, 3)

# 홀수 개를 k번 장대에 옮기고 싶으면, 홀수번째 원판을 k번에 두고 짝수번째 원판을 현재위치와 k번이 아닌 장대에 놓는다.
# 짝수 개를 k번 장대에 옮기고 싶으면, 짝수번째 원판을 k번에 두고 홀수번째 원판을 다른 장대에 놓는다.

# 1의 경우 1을 3번에 둔다
# 2의 경우 1을 2번에 두고
#          2를 3번에 두고 1을 3번에 둔다
# 3의 경우 1을 3번에 두고
#          2를 2번에 두고 1을 2번에 두고
#          3을 3번에 두고 1을 1번에 두고 2를 3번에 두고 1을 3번에 둔다
# 4의 경우 1을 2번에 두고
#          2를 3번에 두고 1을 3번에 두고
#          3을 2번에 두고 1을 1번에 두고 2를 2번에 두고 1을 2번에 두고
#          4를 3번에 두고 1을 3번에 두고 2를 1번에 두고 1을 1번에 두고 3을 3번에 두고 1을 2번에 두고 2를 3번에 두고 1을 3번에 둔다.
N = 3
stack = [1] * (N + 1)
K = 0
result = []
def hanoi(n, d, c): # 원판의 개수, 목표 장대, 현재 장대
    global K
    if n == 1:
        stack[1] = d
        result.append((c, d))
        K += 1
        return
    # 전체 장대에서 현재 장대와 목표 장대 제거
    extra = [1, 2, 3]
    extra.remove(d)
    extra.remove(c)
    hanoi(n - 1, extra[0], stack[n-1])
    stack[n] = d
    result.append((c, d))
    K += 1
    hanoi(n - 1, d, stack[n-1])
hanoi(N, 3, 1)
print(K)
for i in range(K):
    print(*result[i])