# Prim

```python
def prim(start):
    D[start] = 0 # INF -> 0으로 변환
    
    # MST에 포함되지 않은 정점 중에서 거리가 최소인 정점 찾기
    for _ in range(V): # 모든 정점만큼 반복.
        # 거리가 가장 짧은 간선과 그 정점를 찾는다
        min_v = 0 		# 가장 거리가 짧은 간선과 연결된 정점
        min_d = INF 	# 가장 거리가 짧은 간선의 길이
        
        for i in range(1, V+1): # 시작점을 제외한 모든 정점에 대해서
            if MST[i] == 0: # MST에 선택되지 않은 정점이고
                if D[i] < min_d: # 저장된 제일 짧은 거리보다 거리가 짧을때
                    min_d = D[i]
                    min_v = i
        # MST와 연결하기
        MST[min_v] = 1
        for v in range(V+1): # 모든 정점들에 대해서
            # 선택된 정점 min_v와 연결되어있고, 아직 MST에 연결되어있지 않을 때,
            if adj[min_v][v] and not MST[v]:
                if D[v] > adj[min_v][v]:
                    D[v] = adj[min_v][v]		# 최소거리 갱신
                    P[v] = min_v						# 부모 갱신
    return sum(D[start:])
        

V, E = map(int, input().split()) # 노드의 개수, 간선의 개수
INF = 987654321

adj [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    s, e, d map(int, input().split()) # 시작점, 끝점, 가중치
    adj[s][e] = d
    adj[e][s] = d

MST = [0] * (V+1) 	# MST 구성 여부
D = [INF] * (V+1) 	# 최소 거리 저장
P = [0] * (V+1) 		# 연결된 부모

res = prim(1)
print(res)
```



# KRUSKAL

1) 모든 간선 가중치를 오름차순으로 정렬

2. 가중치가 낮은 간선부터 선택하면서 트리를 증가시킴
   - 사이클이 존재하면 제외 -> find_set()을 이용해서 같은 부모를 가지고 있는지 확인
   - 존재하지 않다면 연결 -> union() 
3. n-1 개의 간선이 선택될 때까지 2를 반복

```python
def find_set(x):
    while x != P[x]:
        x = P[x]
    return x

V, E = map(int, input().split())
edge = []
for _ in range(E):
    s, e, d = map(int, input().split())
    edge.append((d, s, e)) # 거리를 앞에 넣어서 sort 함수로 편하게 정렬가능

# 거리를 기준으로 오름차순 정렬
edge.sort()

P = [i for i in range(V+1)]  # 부모 원소 초기화(make_set)
count = 0  # 현재 선택된 정점의 수
total = 0  # 거리의 합

for d, s, e in edge:
    x = find_set(s)
    y = find_set(e)
    if x != y: # 사이클을 형성하지 않음
        count += 1
        total += d
        P[y] = x  # 부모원소를 갱신
        
        if count == V:
            break

```



# Dijkstra

간선의 가중치가 있는 그래프에서 두 정점 사이의 거리가 최소인 경로를 구하는 방식

```python
def digkstra():
    while Q:
        new, dist = Q.pop()
        
        if D[now] < dist: # 주어진 거리보다 이미 저장된 거리가 더 작으면 skip
            continue
        visited[now] = True
        # 현재 정점의 인접 정점을 선택하여 그 인접 정점을 확인
        for v in range(len(adj[now])):
            n_v, n_dist = adj[now][v]
            if not visited[n_v]:
                if dist + n_dist < D[n_v]:
                    D[n_v] = dist + n_dist
                    Q.append(n_v, D[n_v])
    
V, E = map(int, input().split())
# 인접 리스트
sdj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    adj[s].append((e, d))
INF = 987654321
D = [INF] * (V+1)
D[0] = 0
# 시작 정점에서 인접한 정점 거리를 저장
for v, d in adj[0]:
    D[v] = d

visited = [False] * (V+1)
visited[0] = True

Q = [*adj[0]]
digkstra()
```

