start = 'e4'

cnt = 0  # 나이트가 이동할 수 있는 경우의 수
d = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

# 시작 위치를 i, j로 표시
i = ord(start[0]) - ord('a')
j = int(start[1]) - 1

# 포문을 이용해서 8가지 방향에 대해 놓을 수 있는지 세기
for di, dj in d:
    ni, nj = i + di, j + dj
    if 0<=ni<8 and 0<=nj<8:
        cnt += 1

print(cnt)