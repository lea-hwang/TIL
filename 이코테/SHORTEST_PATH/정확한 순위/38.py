# 6명의 학생 중 6번만 성적 비교

# 본인보다 성적이 낮은 학생 수 + 본인보다 성적이 높은 학생 수 == 5
# 플로이드 워셜 ->
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split()) # 학생들 수, 두 학생의 성적을 비교한 횟수
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]     # 인접 노드 정보

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = 1

for i in range(1, N+1):
    graph[i][i] = 0

for mid in range(1, N+1):
    for start in range(1, N+1):
        if start == mid:
            continue
        for end in range(1, N+1):
            if end == mid:
                continue
            if graph[start][mid] == INF or graph[mid][end] == INF:
                continue
            elif graph[start][mid] + graph[mid][end] < graph[start][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

student = 0
for i in range(1, N+1):
    is_known = False
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            is_known = True
        else:
            is_known = False
            break
    if is_known:
        student += 1

print(student)

