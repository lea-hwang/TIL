import sys
sys.stdin = open('2609_input.txt', 'r')

A, B = map(int, input().split())
if A < B:
    A, B = B, A
# A가 무조건 크도록
tmp_A = A
tmp_B = B
while True:
    if tmp_A % tmp_B == 0:
        break
    else:
        tmp_A, tmp_B = tmp_B, tmp_A % tmp_B
print(tmp_B)
print((A//tmp_B) * B)