import sys
sys.stdin = open("9095_input.txt")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    a = [0] * max(4, n+1)
    a[1] = 1
    a[2] = 2
    a[3] = 4
    for j in range(4, n+1):
        a[j] = a[j-1] + a[j-2] + a[j-3]
       
    print(a[n])