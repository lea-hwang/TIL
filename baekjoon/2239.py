import sys
sys.stdin = open('input.txt', 'r')

def find_numbers():
    nums =

sudoku = [list(map(int, input())) for _ in range(9)]


# 1. 들어갈 수 있는 숫자들을 각 칸 별로 구하는 방법
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0: # 만약 스도쿠 숫자가 비어져 있을때


# 2. 가장 경우의 수가 낮은 칸을 찾아서 먼저 채우는 방식
