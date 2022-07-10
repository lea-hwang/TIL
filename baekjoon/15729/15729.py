# 유형: 그리디
# 풀이방법:
# 왼쪽에서부터 버튼을 비교해가며 누른다.
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
btns = [0] * N

cnt = 0

for i in range(N):
    if btns[i] != nums[i]:
        btns[i] = not btns[i]
        if i+1 < N:
            btns[i+1] = not btns[i+1]
        if i + 2 < N:
            btns[i+2] = not btns[i+2]
        cnt += 1
print(cnt)