import sys
sys.stdin = open('2580_input.txt','r')

# 각 행과 열에 안 채워진 숫자를 찾는다 r_empty / c_empty -> set으로 넣을 것
# 빈칸들을 모두 empty_list에 넣는다
# 빈칸들의 개수를 empty에 넣는다.


def dfs(i): # 빈칸의 인덱스와 빈칸의 개수를 받는다
    global empty
    if i == empty: return True  # 만약 빈칸이 0 -> 스도쿠가 채워졌다면 True를 반환한다.

    row, col = empty_list[i] # 현재 빈칸의 행, 열 값
    num_set = [0] * 10 # 현재 행과 열을 기준으로 들어갈 수 있는 수
    for idx in range(1, 10):
        if r_empty[row][idx] == 0 and c_empty[col][idx] == 0 and s_empty[(row//3)*3 + (col//3)][idx] == 0:
            num_set[idx] = 1
    for num in range(1, 10): # 들어갈 수 있는 수 중 하나를 뽑는다
        if num_set[num] == 0:
            continue
        sudoku[row][col] = num      # 스도쿠에 넣는다

        # 아직 넣지 않은 숫자 리스트에서 제외시킨다
        r_empty[row][num] = 1       # 행
        c_empty[col][num] = 1       # 열
        s_empty[(row//3) * 3 + (col//3)][num] = 1 # 3*3 정사각형

        if dfs(i+1): return True # 만약 해답일 경우 True를 반환한다

        # 넣은 숫자가 해답이 아닐 경우 아직 넣지 않은 숫자 리스트에 다시 포함시킨다
        r_empty[row][num] = 0       # 행
        c_empty[col][num] = 0       # 열
        s_empty[(row//3) * 3 + (col//3)][num] = 0 # 3*3 정사각형
        sudoku[row][col] = 0        # 채웠던 칸 다시 0으로 돌려놓는다
    return False


# ------ 여기서 시작 ------
sudoku = [0] * 9 # 스도쿠 퍼즐
r_empty = [[0]*10 for _ in range(9)] # 각 행에서 안채워진 숫자
c_empty = [[0]*10 for _ in range(9)] # 각 열에서 안채워진 숫자
s_empty = [[0]*10 for _ in range(9)] # 3*3 정사각형 내에서 안채워진 숫자
empty_list = [0] * 81 # 빈칸이 튜플 형태로 존재
empty = 0  # 빈칸의 수

for i in range(9):
    sudoku[i] = list(map(int, input().split()))
    for j in range(9):
        now = sudoku[i][j]
        if now: # 해당 행과 열에 해당 숫자를 제외
            r_empty[i][now] = 1
            c_empty[j][now] = 1
            s_empty[(i//3)*3 + (j//3)][now] = 1
        else:
            empty_list[empty] = (i, j)
            empty += 1
dfs(0)

for i in range(9):
    print(*sudoku[i])


