import sys
sys.stdin = open('2751_input.txt', 'r')

N = int(input())
arr = [0] * N
for i in range(N):
    #arr[i] = int(sys.stdin.readline().rstrip())
    arr[i] = int(input())
arr.sort()

for i in range(N):
    print(arr[i])
