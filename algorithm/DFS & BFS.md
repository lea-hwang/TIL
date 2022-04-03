# DFS & BFS

내용이 올바르지 않다고 생각한다면, 주저없이 말씀해주시면 감사하겠습니다.

1. DFS or BFS 어떤 걸 쓰면 좋을까?

   - 문제 마다 다르다! 어떤 문제는 DFS로, 어떤 문제는 BFS로 풀었을 때 더 효율적일 수 있기 때문에 문제를 많이 접해보고 그 문제에 해당하는 풀이를 생각해야한다.

   - 이건 필자가 생각하는 DFS로 풀어야하는 문제들이다.
     - [연산자 끼워넣기](https://www.acmicpc.net/problem/14888)
     - [배열 최소 합](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)
     - 주로 순열을 이용을 하거나, 

   - 이건 필자가 생각하는 BFS로 풀어야하는 문제들이다.
     - [특정 거리의 도시 찾기](https://www.acmicpc.net/problem/18352)
     - [홈 방범 서비스](https://swexpertacademy.com/main/code/problem/problemDetail.do)
     - 최단거리, 최소 연산 등 최소한의 연산이나 행동 횟수를 구하는 문제들이 많다. 혹은 특정 횟수에서의 모든 경우를 파악하고 싶을때 주로 사용한다.
     - DFS로 풀 수 있을 수도 있지만, BFS보다 비효율적일 가능성이 높다.(가지치기를 적절히 할 수 있다면 DFS로 풀 수 있을 수도 있다~)

   - 이건 필자가 생각하는 DFS, BFS 모두 가능한 문제들이다.
     - [단지번호붙이기](https://www.acmicpc.net/problem/2667)
     - [바이러스](https://www.acmicpc.net/problem/2606)
     - [연구소](https://www.acmicpc.net/problem/14502)
     - DFS, BFS 탐색방법을 정하는게 의미가 없는 문제들일 가능성이 높다. 
     - 주로 브루트포스 알고리즘을 이용해야 하는, 즉 전체탐색을 해봐야 하는 문제들이다.
     - 그저 현재 위치에서 갈 수 있는 모든 길을 가기만 하면 목적을 달성하는 문제들이라고 생각한다.

2. 어떤 식으로 풀면 좋을까...?
   1. 처음, DFS나 BFS가 익숙하지 않을 때는 템플릿을 외우는 것을 추천한다. 백준에서 브론즈~ 실버 정도의 가장 기본적인 BFS, DFS 문제를 풀면서 해당 템플릿이 어떻게 적용되고 있는지 익힌다.
   2. 해당 템플릿이 어떤 요소를 위해 작성되어 있는지 다시 살펴본다. 처음 템플릿을 

1. DFS
   1. 구성요소(템플릿)
   2. 각 구성요소를 문제별로 어떻게 적용할 수 있을까?
   3. 재귀와 스택 중 어떤 것을 쓰는게 좋을까?
2. BFS
   1. 구성요소(템플릿)
   2. 각 구성요소를 문제별로 어떻게 적용할 수 있을까?
   3. 재귀와 큐 중 어떤 것을 선택해야할까?



# DFS

: 깊이 우선 탐색. 즉, 연결되어있는 길을 쭈욱 따라간다고 생각하면 편하다. 트리나 그래프에서 연결된 모든 노드를 되돌아가기 없이 탐색하다가, 더이상 탐색할 노드가 없을 때 이전 노드의 새로운 길을 탐색하는 형태라고 생각하자.

```python
# 
def DFS(start, N):
  	stack = []
    visited = [0] * N
    
    stack.append(start)
    visited[start] = 1
    
    while stack:
      	# 현재 위치
      	v = stack.pop()
        
        # 종료 조건 ~~
        
        
        # 현재 위치를 기준으로 다음 위치를 찾는다
        for nxt in range(N):
          	if not visited[nxt]:
              	stack.append(nxt)
                visited[nxt] = 1
```







# BFS