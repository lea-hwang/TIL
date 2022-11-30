import sys
sys.stdin = open("input.txt")

R, C = map(int, input().split())

# 입력을 받는다.
mat = [list(input()) for i in range(R)]

# 우 좌 하 상
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
pipe = {'|': [2, 3], '-': [0, 1], '+': [0, 1, 2, 3], '1': [1, 3], '2': [1, 2], '3': [0, 2], '4': [0, 3]}
pipe2 = {(2, 3): '|', (0, 1): '-', (0, 1, 2, 3): '+', (0, 2): '1', (0, 3): '2', (1, 3):'3', (1, 2):'4'}

direction = []
pi, pj = 0, 0

def find():
    global R, C, direction, pipe, mat, pi, pj
    for ci in range(R):
        for cj in range(C):
            if mat[ci][cj] == '.':
                check = False
                for idx in range(4):
                    ni, nj = ci + di[idx], cj + dj[idx]
                    if 0 <= ni < R and 0 <= nj < C:
                        shape = mat[ni][nj]
                        if shape == '.' or shape == 'M' or shape == 'Z':
                            continue
                        if idx in pipe[shape]:
                            check = True
                            direction.append(idx)
                if check and len(direction) > 1:
                    pi, pj= ci, cj
                    return
                else:
                    direction = []
find()
for key in pipe2.keys():
    if key == tuple(direction):
        print(pi + 1, pj + 1, pipe2[tuple(direction)])
