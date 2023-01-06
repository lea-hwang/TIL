import sys
sys.stdin = open("input.txt")

def recursive(n):
    if n == 0:
        return '*'

    prev_mat = recursive(n-1)
    mat = []
    for line in prev_mat:
        mat.append(line + line)

    for line in prev_mat:
        mat.append(line + ' ' * (2**(n-1)))

    return mat

n = int(input())
result = recursive(n)
for line in result:
    print(line.rstrip())