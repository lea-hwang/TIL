# 40분
# 괄호의 개수가 n개라면 총 2^n - 1 개의 새로운 식을 만들 수 있음
# (를 만났을 경우, 괄호의 순서(1,2,3번째)를 스택에 담고 그 순서를 배열에 저장하고, )를 만났을 경우 제일 상단에 있는 숫자를 꺼내서 배열에 저장한다
import sys
sys.stdin = open("input.txt")
from itertools import combinations

# 식 입력받기
formula = input()
# 각 괄호를 구분하기 위해 1, 2, 3 .. 번째 순서 매기기
p = [0] * len(formula)
# (가 들어올 때, 괄호 순서를 저장할 스택
stack = []
# 괄호 순서(1,2,3 ...으로 커짐)
turn = 0

# 먼저 각 괄호 위치를 파악
for idx, char in enumerate(formula):
    if char == '(':
        turn += 1
        stack.append(turn)
        p[idx] = turn
    elif char == ')':
        p[idx] = stack.pop()

# n개의 괄호를 지우기 위해 2^n -1 개의 부분집합을 생성
delete_p_list = []

for i in range(1, turn+1):
    delete_p_list.extend(list(combinations(range(1, turn+1), i)))

# 만약 해당 괄호가 부분집합 내에 있을 경우, 해당 괄호를 제외하고 출력
results = []
for nums in delete_p_list:
    line = []
    for idx, letter in enumerate(formula):
        if p[idx] in nums:
            continue
        line.append(letter)
    results.append(''.join(line))

# 중복되는 값 제거 및 사전순으로 정렬
results = sorted(list(set(results)))
for result in results:
    print(result)
