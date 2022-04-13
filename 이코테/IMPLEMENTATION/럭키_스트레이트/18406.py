import sys
sys.stdin = open('input.txt', 'r')
num = input()

left = 0
right = 0
N = len(num)//2
for i in range(N):
    left += int(num[i])
    right += int(num[-i-1])

if left == right:
    print("LUCKY")
else:
    print("READY")