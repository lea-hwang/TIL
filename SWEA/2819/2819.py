import sys
sys.stdin = open('2819_input.txt', 'r')



def DFS(i, j, n, num): # 시작점, 종료조건, 넘겨줄 숫자
    if n == 7:
        nums.add(num)
        return

    for d_i, d_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        n_i = i + d_i
        n_j = j + d_j
        if 0 <= n_i < 4 and 0 <= n_j < 4:
            DFS(n_i, n_j, n+1, num * 10 + grid[n_i][n_j])


T = int(input())
for tc in range(1, T+1):
    grid = [list(map(int, input().split())) for _ in range(4)]
    nums = set()
    for i in range(4):
        for j in range(4):
            DFS(i, j, 0, 0)
    print(f'#{tc} {len(nums)}')