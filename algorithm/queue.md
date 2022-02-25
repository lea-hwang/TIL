# 큐(Queue)

> 삽입한 순서대로 원소가 저장되어 가장 먼저 삽입(First In) 된 원소는 가장 먼저 삭제(First Out)됨

- 구조
  - 머리(Front): 저장된 원소 중 첫 번째 원소
  - 꼬리(Rear): 저장된 원소 중 마지막 원소
- 주요연산
  - enQueue(item): 큐의 뒤쪽(rear 다음)에 원소를 삽입
  - deQueue(): 큐의 앞쪽(front)에서 원소를 삭제하고 반환
  - createQueue(): 공백 상태의 큐를 생성
  - isEmpty(): 큐가 공백상태인지를 확인
  - isFull(): 큐가 포화상태인지를 확인
  - Qpeek(): 큐가 앞쪽(front)에서 원소를 삭제 없이 반환



## 선형 큐

> 1차원 배열을 이용한 큐

- 큐의 크기 = 배열의 크기

- front: 저장된 첫 번째 원소의 인덱스

- rear: 저장된 마지막 원소의 인덱스

- 상태표현

  - 초기 상태: front = rear = -1
  - 공백 상태: front == rear
  - 포화 상태: rear == n-1(n: 배열의 크기)

- 처음 : front = rear = -1 로 초기화

- 삽입: enQueue(item)

  > 마지막 원소 뒤에 새로운 원소 삽입

  - rear 값을 하나 증가시켜 새로운 삽입할 자리를 마련

  - 그 인덱스에 해당하는 배열원소를 Q[rear]에 item을 저장

  - 예시

    ```python
    def enQueue(item):
        global rear
        if isFull(): print("Queue_Full")
        else:
            rear += 1
            Q[rear] = item
    ```

- 삭제: deQueue()

  > 가장 앞에 있는 원소를 삭제

  - front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소로 이동

  - 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능

  - 예시

    ```python
    def deQueue():
        if isEmpty(): print("Queue_Empty")
        else:
            front += 1
            return Q[front]
    ```

- 공백상태, 포화상태 검사: isEmpty(), isFull()

  - 공백상태: front == rear

  - 포화상태: rear == n-1

  - 예시

    ```python
    def isEmpty():
        return front == rear
    def isFull():
        return rear == len(Q) - 1
    ```

- 검색: Qpeek()

  > 가장 앞에 있는 원소를 검색하여 반환

  - 현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환

    ```python
    def Qpeek():
        if isEmpty(): print("Queue_Empty")
        else: return Q[front+1]
    ```

    

## 원형 큐

> 1차원 배열을 사용하되, 배열의 처음과 끝이 연결되어 원형형태를 큐를 이룬다고 가정하고 사용

- 초기 공백 상태
  - front = rear = 0
- index의 순환
- front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동
- front 변수
  - 공백상태화 포화상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

- 삽입 위치 및 삭제 위치

  - 삽입 위치: rear = (rear+1) % n
  - 삭제 위치: front = (front+1) % n

- 구현

  - 처음 : front = rear = 0 로 초기화

  - 공백상태 및 포화상태 검사: isEmpty(), isFull()

    - 공백상태: front == rear

    - 포화상태: 삽입할 rear 다음 위치 == 현재 front

      - (rear+1) % n = front

    - 예시

      ```python
      def isEmpty():
          return front == rear
      def isFull():
          return (rear+1) % len(cQ) == front
      ```

  - 삽입: enQueue(item)

    > 마지막 원소 뒤에 새로운 원소를 삽입

    - rear 값을 조정하여 새로운 원소를 삽입합 자리를 마련함 rear = (rear+1) % n

    - 그 인덱스에 해당하는 배열원소 cQ[rear]에 item을 저장

    - 예시

      ```python
      def enQueue(item):
          global rear
          if isFull():
              print("Queue_Full")
          else:
              rear = (rear+1) % len(cQ)
              cQ[rear] = item
      ```

  - 삭제: deQueue(), delete()

    > 가장 앞에 있는 원소를 삭제

    - front 값을 조정하여 삭제할 자리를 마련함

    - 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능함

    - 예시

      ```python
      def deQueue():
          global front
          if isEmpty(): print("Queue_Empty")
          else:
              front = (front + 1) % len(cQ)
              return cQ[front]
      ```



## 우선순위 큐(Priority Queue)

> 우선 순위를 가진 항목들을 저장하는 큐
>
> 우선 순위가 높은 순서대로 먼저 나가게 됨

- 적용 분야
  - 시뮬레이션 시스템
  - 네트워크 트레픽 제어
  - 운영체제의 테스크 스케줄링

## 버퍼(Buffer)

> 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역

- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다

- 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용된다



## BFS(Breadth First Search)

> 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함

- 예시

  ```python
  def BFS(G,v): # 그래프 G, 탐색 시작점 v
  	visited = [0]*(n+1) 	# n: 정점의 개수
  	Q = []					# 큐 생성
  	Q.append(v)				# 시작점 v를 큐에 삽입
  	while Q:				# 큐가 비어있지 않은 경우
  		t = queue.pop(0)	# 큐의 첫번째 원소 반환
  		if not visited[t]:		# 방문되지 않은 곳이라면
  			visieted[t] = True 	# 방문한 것으로 표시
  			visit(t)			# 정점 t에서 할 일
  		for i in G[t]: # t와 연결된 모든 정점에 대해
  			if not visited[i]: 	# 방문되지 않은 곳이라면
  				Q.append(i)		# 큐에 모두 넣기
  ```

- while 이전에는 

  - visited 배열 초기화
  - Q 생성
  - 시작점 enqueue

- while은 Q가 비어있지 않으면 돌아감

  - dequeue A
  - A 방문한 것으로 표시
  - A의 인접점 enqueue

- 큐에 중복적으로 들어가는 것을 방지하기위해, 큐에 들어갔을때 visited를 남김

- 예시

  ```python
  def BFS(G, v, n): # 그래프 G, 탐색 시작점 v
      visited = [0] * (n+1) 	# n : 정점의 개수
      Q = []					# 큐 생성
      Q.append(v)				# 시작점 v를 큐에 삽입
      visited[v] = 1
      while Q: 			# 큐가 비어있지 않은 경우
          t = Q.pop(0)	# 큐의 첫번째 원소 반환
          visit(t)
          for i in G[t]: 			# t와 연결된 모든 정점에 대해
              if not visited[i]: 	# 방문되지 않은 곳이라면 
                  Q.append(i) 	# 큐에 널기
                  visited[i] = visited[t] + 1 # t으로부터 1만큼 이동
  ```

  

## 미로 탐색

- 출발- 도착 최단거리

  ```python
  def BFS(G, v, n): # 그래프 G, 탐색 시작점 v
      visited = [0]*(n+1) # n: 정점의 개수
      queue = []			# 큐 생성
      queue.append(v)		# 시작점 v를 큐에 삽입
      visited[v] = 1
      while queue: 			# 큐가 비어있지 않은 경우
          t = queue.pop(0) 	# 큐의 첫번째 원소 반환
          visit(t)			# 방문이 아니라 어떤 일을 처리한다-> 목적지인지 판단한다 
          for i in G[t] :         # t와 연결된 모든 정점에 대해
              if not visited[i]: 	# 방문되지 않은 곳이라면
                  queue.append(i) # 큐에 넣기
                  visited[i] = visited[t] + 1 # t로부터 1만큼 이동
  ```

  