import sys
sys.stdin = open('input.txt', 'r')



N = int(input())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
scores = [0] * N
scores[0] = stairs[0]

if N > 1:
    scores[1] = stairs[1] + stairs[0]
if N > 2:
    scores[2] = max(stairs[1], stairs[0]) + stairs[2]
if N > 3:
    for i in range(3, N):
        scores[i] = max(scores[i-3] + stairs[i-1], scores[i-2]) + stairs[i]

print(scores[N-1])
