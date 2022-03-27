import sys
sys.stdin = open('1780_input.txt', 'r')

def paper(i, j, N): # 시작점 (i, j), matrix의 크기
    num = matrix[i][j]
    is_paper = True
    # 처음부터 끝까지 돌다가 만약 같지 않은 수를 발견할 경우
    for row in range(i, i+N):
        for col in range(j, j+N):
            if matrix[row][col] != num:
                is_paper = False
                break
        if not is_paper:
            break
    else: # 모든 숫자가 같을 때
        cnt[num] += 1
        return
    # 모든 숫자가 같지 않을 때
    for row in range(i, i+N, N//3):
        for col in range(j, j+N, N//3):
            paper(row, col, N//3)
    return

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

cnt = [0, 0, 0] # 0, 1, -1로 채워진 종이의 개수
paper(0, 0, N)

print(cnt[-1])
print(cnt[0])
print(cnt[1])
