## DFS(깊이 우선 탐색)

> 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아 와서다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
>
> **후입선출 구조의 스택 사용**

- 알고리즘

  1. 시작 정점 v를 결정하여 방문한다.
  2. 정점 v에 인접한 정점 중에서 
     - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2.를 반복한다.
     - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2를 반복한다.

  3. 스택이 공백이 될 때까지 2.를 반복한다.

  ```python
  N, E = map(int, input().split()) # 노드의 개수, 간선의 개수
  edges = list(map(int, input().split())) # 간선(쌍으로 존재)
  
  # 방문 경로를 저장할 2차원 리스트
  G = [[0] * (N+1) for _ in range(N+1)]
  # G[출발점][도착점] = 1
  # G[도착점][출발점] = 1
  for idx in range(E):
      # edges[idx*2] 출발점, edges[idx*2+1] 도착점
      G[edges[idx*2]][edges[idx*2 + 1]] = 1
      G[edges[idx*2 + 1]][edges[idx*2]] = 1
  
  visited = [False] * (N + 1)
  stack = []
  top = -1
  
  v = edges[0]
  visited[v] = True
  stack.append(v)
  while(stack):
      v = stack.pop()
      if visited[v] == 0:		# 방문했는지 확인
  	    visited[w] = True	# 방문으로 수정
      # 다음 갈 수 있는 노드를 탐색 G에 인접 노드 정보가 들어있다.
      # G[출발][도착] == 1이면 이동가능한 노드
      for nxt in range(N, -1, -1):
          if G[v][nxt] == 1 and visited[nxt] == 0:
              stack.append(nxt)
  ```


## 부분집합의 합

트리로 구현

## 퀵정렬(Quick Sort)

```python
def partition(a, begin, end):
    pivot = (begin + end)//2
    L = begin
    R = end
    while L < R:
        while(L<R and a[L] <  a[pivot]): L += 1 # 왼쪽에서 pivot보다 크거나 같은 값을 찾는다
        while(L<R and a[R] >= a[pivot]): R -= 1 # 오른쪽에서 pivot보다 작은 값을 찾는다
        if L == R: pivot = R
        a[L], a[R] = a[R], a[L]
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
```

