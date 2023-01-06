import sys
sys.stdin = open(("input.txt"))

n = int(input())

def recursive(n, step):
    diff = (n - step) * 2
    if step == 1:
        mat[diff][diff], mat[diff + 1][diff], mat[diff + 2][diff] = ['*'] * 3
        return

    recursive(n, step-1)

    row, col = 4 * step - 1, 4 * (step-1) + 1
    for j in range(diff, diff + col):
        mat[diff][j] = '*'
        mat[-diff-1][j] = '*'
    for i in range(diff + 1, diff + row-1):
        mat[i][diff] = '*'
        mat[i][-diff-1] = '*'
    mat[diff + 1][-diff-1] = ' '
    mat[diff + 2][-diff-2] = '*'

if n == 1:
    print('*')
else:
    mat = [[' '] * (4 * (n-1) + 1) for _ in range(4 * n -1)]
    recursive(n, n)
    for line in mat:
        print(''.join(line).rstrip())


