import sys
sys.stdin = open('15829_input.txt', 'r')

N = int(input())
letters = input()
H = 0
M = 1234567891

for i in range(N):
    a = ord(letters[i]) - ord('a') + 1
    r = 31
    H += a * 31**i

H %= M

print(H)