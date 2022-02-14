# APS

## 배열 : 2차원 배열

- 선언

  - 1차원 List를 묶어놓은 List
  - 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
  - 2차원 List의 선언: 세로 길이(행의 개수), 가로길이(열의 개수)를 필요로 함
  - Python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

- 접근

  - 배열 순회

    - n*m 배열의 n\*m 개의 모든 원소를 빠짐없이 조사하는 방법

    - 행 우선 순회

      ```python
      # i 행의 좌표
      # j 열의 좌표
      for i in range(n):
          for j in range(m):
          	Array[i][j] # 필요한 연산 수행
      ```

    - 열 우선 순회

      ```python
      # i 행의 좌표
      # j 열의 좌표
      for j in range(m):
          for i in range(n):
              Array[i][j] # 필요한 연산 수행
      ```

    - 지그재그 순회

      > 거꾸로는 m-1-j

      ```python
      # i 행의 좌표
      # j 열의 좌표
      for i in range(n):
          for j in range(m):
        		Array[i][j + (m-1-2*j) * (i%2)]
      ```

    - 델타를 이용한 2차 배열 탐색

      - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

      ```python
      arr[0...N-1][0...N-1] # N*N 배열
      di[] <- [0, 0, -1, -1] # 좌우상하
      dj[] <- [-1, 1, 0, 0]
      for i in range(N):
          for j in range(N):
              for k in range(4):
                  ni <- i + di[k]
                  nj <- j + dj[k]
                  if 0<=ni<N and 0<=nj<N # 유효한 인덱스면
                      	test(arr)
      ```

    
    - dd
    
      ```python
      # i : 행의 좌표, len(arr)
      # j : 열의 좌표, len(arr[0])
      arr = [[1,2,3], [4,5,6], [7,8,9]] # 3*3 행렬
      for i in range(3):
          for j in range(3):
              if i < j:
                  arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
          # for j in range(i+1,3):
          	arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
      ```
    
      

## 부분집합 생성

- 부분집합의 수

  - 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n개이다.

  ```python
  A = [1,2,3]
  bit = [0]*3
  for i in range(2):
      bit[0] = i
      for j in range(2):
          bit[1] = j
          for k in range(2):
              bit[2] = k
              for p in range(3):
                  if bit[p]:
  		            print(A[p], end = ' ')
      print()
      
  ```

  ```python
  arr = [3,6,7,1,5,4]
  n = len(arr)
  for i in range(1<<n):
      for j in range(n):
          if i & (1<<j):
              print(arr[j], end=", ")
      print()
  print()
  ```



- 순차검색(Sequential Search)

  - 일렬로 되어 있는 자룔르 순서대로 검색하는 방법

    - 가장 간단하고 직관적인 검색 방법

    - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
    - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임

  - 2가지 경우

    - 정렬이 되어있지 않는 경우

      - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.

      - 키 값이 동일한 원소를 찾으면 해당 인덱스를 반환한다.

      - 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

      - 찾고자 하는 원소의 순서에 따라 비교횟수가 결정됨

        - 첫 번째 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번 비교

        - 정렬되지 않은 자료에서의 순차 검색의 평균 비교 횟수

          = (1/n)

        - 시간 복잡도: O(n)

        - 예시

          ```python
          def sequentialSearch(a, n, key):
              i = 0
              while i<n and a[i]!=key: # 인덱스 에러 방지
                  i += 1
              if i<n: return i
              else: return -1
          ```

          

    - 정렬이 되어 있는 경우

      - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정

      - 자료를 순차적으로 검색하면서 키 값을 비교하며, 원소의 키 값이 검색대상의 키 값보다 크면, 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.

      - 찾고자 하는 ㅝㄴ소의 순서에 따라 비교횟수가 결정됨

      - 정렬되어있으므로 검색 실패를 반환하는 경우, 평균 비교 횟수가 반으로 줄어든다.

      - 시간복잡도 O(n)

        ```python
        def sequentialSearch2(a, n, key):
            i=0
            while i<n and a[i]<key :
                i += 1
                
        ```

      - 

## 바이너리 서치 (Binary Search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 번위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

- 검색 과정

  - 자료의 중앙에 있는 원소를 고른다

  - 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.

  - 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.

  - 찾고자 하는 값을 찾을때 까지 과정을 반복한다.

  - 구현

    - 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다.
    - 이진 검색의 경우, 자료의 삽입이나 삭제가 발생했을 때 배열이ㅡ 상태를 항상

    ```python
    def binarySearch(a, N, key):
        start = 0
        end = N-1
        while start <= end:
            middle = (stard + end) //2
            if a[middle] == key : # 검색 성공
                return True
            elif a[middle] > key: # 검색 실패
                end =  middle -1
            else: start = middle =  middle + 1
        return False
    ```

### 인덱스



## 셀렉션 알고리즘 (Selection Algorithm)

- 

## 선택 정렬(Selection Sort)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

  - 앞서 살펴본 셀렉션 알고리즘을 전체 자료에 적용한 것이다

- 정렬과정

  1. 주어진 리스트 중에서 최소값을 찾는다.

  2. 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.

  3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

- 시간 복잡도

  - O(n^2)

  ```python
  def selectionSort(a, N):
      for i in range(N-1):
          minIdx = i
          for j in range(i+1, N):
              if a[minIdx] > a[j]:
                  minIdx = j
          a[i], a[minIdx] = a[minIdx], a[i]
  ```

  

