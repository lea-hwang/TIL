import sys
sys.stdin = open('1931_input.txt', 'r')

N = int(input()) # 회의의 수
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda meeting: (meeting[1], meeting[0]))

end = 0
total = 0
i = 0
while i < N:
    if end <= meetings[i][0]:
        total += 1
        end = meetings[i][1]
    i += 1

print(total)