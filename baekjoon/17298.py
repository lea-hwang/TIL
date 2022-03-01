import sys
sys.stdin = open('17298_input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))

bigger = [0] * N    # 오큰수를 저장할 리스트
stack = [A[N-1]]    # 큰수들을 오름차순으로 저장할 스택
bigger[N-1] = -1    # 가장 마지막 수는 오큰수가 없음
for i in range(N-2, -1, -1):
    if A[i] < stack[-1]: # i번째 수가 top보다 작을 경우(오름차순)
        bigger[i] = stack[-1]
    else: # i번째 수가 top보다 크거나 같을 경우
        while stack and stack[-1] <= A[i]: # 본인보다 더 큰 수가 나올때 까지 pop
            stack.pop()
        if stack: # 만약 stack에 본인보다 더 큰 수가 남아있다면
            bigger[i] = stack[-1]
        else: # 비어있다면
            bigger[i] = -1
    stack.append(A[i]) # 현재 수 추가
print(*bigger)