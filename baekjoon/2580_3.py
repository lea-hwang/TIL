import sys

sys.stdin = open('2580_input.txt', 'r')


def num_set(i, j):  # 현재 위치에서 넣을 수 있는 숫자를 반환한다.
    nums = [0] + [1] * 9 # 있는 수가 0

    # 현재 row, column에 있는 숫자를 제외시킨다
    for idx in range(9):
        nums[sudoku[i][idx]] = 0
        nums[sudoku[idx][j]] = 0

    # 현재 3*3 내에 있는 숫자를 제외시킨다
    a = (i // 3) * 3
    b = (j // 3) * 3
    for row in range(a, a + 3):
        for col in range(b, b + 3):
            nums[sudoku[row][col]] = 0

    n_set = [k for k in range(10) if nums[k]]
    return n_set


def dfs(n):
    if n == len(empty_list):  # 스도쿠가 다 채워졌다는 것을 의미
        for i in range(9):
            print(*sudoku[i])
        sys.exit(0)
    else:
        row, col = empty_list[n] # 비어있는 칸의 위치
        for now in num_set(row, col): # 비어있는 칸에 넣을 수 있는 숫자를 넣는다
            sudoku[row][col] = now
            dfs(n+1)
            sudoku[row][col] = 0 # 틀렸을 경우 숫자를 다시 제거한다


sudoku = [list(map(int, input().split())) for _ in range(9)]
empty_list = [(i, j) for i in range(9) for j in range(9) if not sudoku[i][j]]  # 비어있는 칸 위치 저장

dfs(0)