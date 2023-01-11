import sys
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)] # 간선의 정보를 담을 리스트

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# print(edges)  [[], [2], [1, 3], [2, 4], [3, 5], [4]]

M = int(input()) # 질문 수
for _ in range(M):
    q_num, k = map(int, input().split())
    # k가 단절점인가?
    if q_num == 1:
        # 현재 연결된 노드가 2개 이상이라면 yes
        if len(edges[k]) >= 2:
            print("yes")
        else:
            print("no")
    # k가 단절선인가?
    else:
        # 트리의 모든 선은 단절선임. 항상 yes.
        print("yes")