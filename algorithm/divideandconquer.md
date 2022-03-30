# 분할과 정복

전략

- 분할(Divide): 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복(Conquer): 나눈 작은 문제를 각각 해결한다.
- 통합(Combine): 해결된 해답을 모은다.

### 병합정렬(Merge Sort)

여러 개의 정렬된 자료의 집합을 병합하여 한 개으 정렬된 집합으로 만드는 방식

#### 과정

- 분할 단계: 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.

- 병합 단계: 2개의 부분집합을 정렬하면서 하나의 집합으로 병합

  ```python
  def merge(left, right):
      result = []
      while len(left) > 0 or len(right) > 0:
          if len(left) > 0 and len(right) > 0:
              if left[0] <= right[0]:
                  result.append(left.pop(0))
              else:
                  result.append(right.pop(0))
          elif len(left) > 0:
              result.extend(left)
          else:
              result.extend(right)
      return result
  
  def merge_sort(arr):
      if len(arr) == 1: return arr
  
      left = []
      right = []
      mid = len(m)//2
      for x in arr[:mid]:
          left.append(x)
      for x in arr[mid:]:
          right.append(x)
      
      left = merge_sort(left)
      right = merge_sort(right)
      
      return merge(left, right)
  ```

  -> 실제로 구현할 때는 리스트를 쪼개는 것이 아닌 인덱스만 전달하여 배열 안의 값들을 바꾸는 형식으로 한다



### 퀵정렬(Quick Sort)

#### Hoare partition

```python
def quick_sort(A, l, r):
    if l < r:
        s = partition(a, l, r)
        quick_sort(A, l, s-1)
        quick_sort(A, s+1, r)

def partition(A, l, r):
    p = A[l]	# 피봇 값
    i = l + 1
    j = r
    while i <= j:
        while i <= j and A[i] <= p: i += 1 # 피봇보다 큰 값을 찾는다
        while i <= j and A[j] >= p: j -= 1 # 피봇보다 작은 값을 찾는다
        if i < j: # 교차되지 않았을 때
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j
```

- 피봇 선택
  - 왼쪽 끝/ 오른쪽 끝/ 임의의 세개 값 중에 중간 값 -> 최악의 경우 방지

#### Lomuto partition

```python
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x: # 더 작은 수라면 i가 j를 따라감
            i += 1
        		A[i], A[j] = A[j], A[i]
    A[i], A[j] = A[j], A[i]
```



### 이진 검색(Binary Search)

자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

#### 과정

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 찾을 때까지 1~3의 과정을 반복한다.

```python
def binary_search(N, key):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid -1
        else:
            start = mid + 1
    return -1
```

```python
def binary_search(start, end, key):
    if start > end:
        return -1
    else:
        mid = (start + end)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binary_search(start, mid-1, key)
        else:
            return binary_search(mid+1, end, key)
```

# 백트래킹

여러 가지 선택지(옵션)들이 존재하는 상황에서 한가지를 선택한다.

```c
bool backtrack(선택 집합, 선택한 수, 모든 선택수){
		if (선택한 수 == 모든 선택 수) // 더이상 탐색할 노드가 없다
		{
				찾는 솔루션인지 체크;
				return 결과;
		}
		현재 선택한 상태집합에 포함되지 않는 후보 선택들(노드) 생성
		
		모든 후보 선택들에 대해
		{
			  선택 집합에 하나의 후보 선택을 추가
			  선택한 수 = 선택한 수 + 1
			  결과 = backtrack 호출(선택집합, 선택한 수, 모든 선택수)
			  if (결과 == 성공){
			  		return 성공; // 성공한 경우 상위로 전달
			  }
			  return 실패;
		}
}
```

```python
def backtrack(a[], k, input):
    c[MAXCANDIATES] # 후보군을 저장할 배열
    ncands # 후보의 수
    if k == input: process_solution()
    else:
      	k += 1
        make_candidate(a[], k, input)
def make_candidate(a[], k, n, c[], ncands):
    c[0] = True
    c[1] = False
    ncands = 2
def process_solution(a[], k)
    for i in range(1, k):
        if a[i]: print(i)
```

순열

1. 자리교환
2. 사용한 숫자 표시
3. 사용하지 않은 목록 만들기

# 트리

