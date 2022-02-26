import sys
#sys.stdin = open('2580_input.txt','r')

# 각 행과 열에 안 채워진 숫자를 찾는다 r_empty / c_empty
# 빈칸들을 모두 empty_list에 넣는다

def dfs(n): # 빈칸의 인덱스와 빈칸의 개수를 받는다
    if n == len(empty_list):
        for i in range(9):
            print(*sudoku[i])
        sys.exit()  # 만약 빈칸이 0 -> 스도쿠가 채워졌다면 끝내기
    row, col = empty_list[n] # 현재 빈칸의 행, 열 값

    for num in range(1, 10): # 들어갈 수 있는 수 중 하나를 뽑는다
        if r_empty[row][num] or c_empty[col][num] or s_empty[s_get[row][col]][num]:
            continue
        sudoku[row][col] = num      # 스도쿠에 넣는다

        # 아직 넣지 않은 숫자 리스트에서 제외시킨다
        r_empty[row][num] = c_empty[col][num] = s_empty[s_get[row][col]][num] = True

        dfs(n+1)

        # 넣은 숫자가 해답이 아닐 경우 아직 넣지 않은 숫자 리스트에 다시 포함시킨다
        r_empty[row][num] = c_empty[col][num] = s_empty[s_get[row][col]][num] = False


# ------ 여기서 시작 ------
sudoku = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)] # 스도쿠 퍼즐
r_empty = [[False]*10 for _ in range(9)] # 각 행에서 안채워진 숫자
c_empty = [[False]*10 for _ in range(9)] # 각 열에서 안채워진 숫자
s_empty = [[False]*10 for _ in range(9)] # 3*3 정사각형 내에서 안채워진 숫자
s_get = [[(i//3) * 3 + (j//3) for j in range(9)] for i in range(9)]
empty_list = [] # 빈칸이 튜플 형태로 존재


for i in range(9):
    for j in range(9):
        now = sudoku[i][j]
        if now: # 해당 행과 열에 해당 숫자를 제외
            r_empty[i][now] = True
            c_empty[j][now] = True
            s_empty[s_get[i][j]][now] = True
        else:
            empty_list.append((i, j))
dfs(0)