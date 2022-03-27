import sys
sys.stdin = open('1715_input.txt', 'r')

N = int(input())
nums = [int(input()) for _ in range(N)]

# 숫자 카드 묶음 정렬
nums.sort()

# 최소 비교 횟수 구하기
# 가장 작은 두 수를 찾아서 더하고 그 값을 다시 배열에 넣은 다음 다시 제일 작은 두 수를 찾아 더한다.
# 최소 힙으로 구현

def enqueue(N):
    # 제일 마지막 자리에 삽입 후
    heap.append(N)
    c = len(heap)-1
    p = c//2
    # 부모 노드와 비교하여 자식노드가 부모 노드보다 작다면 부모노드와 바꿔치기 한다.
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2


def dequeue():
    if len(heap) == 2:
        return heap.pop()
    # 제일 상단의 노드의 값을 저장한다
    root = heap[1]

    # 제일 마지막 노드를 루트에 둔 후
    heap[1] = heap.pop()
    # 자식 노드와 비교하여 자식 노드가 부모 노드보다 작다면 부모노드와 바꿔치기한다.
    p = 1
    c = p*2
    # 왼쪽 자식노드가 존재할 때 실행
    while c < len(heap):
        c2 = p*2+1
        if c2 < len(heap): # 오른쪽 자식 노드가 존재 할때
            # 오른쪽 자식노드가 더 작다면
            if heap[c] > heap[c2]: # c2가 더 작을 때
                c = c2
        # 만약 부모노드가 더 크다면 자식노드와 바꿔치기 함
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p*2
        else:
            break
    return root

heap = [0] + nums # [0, 10, 20, 40]

total = 0
while len(heap) > 2:
    # 가장 작은 두 수를 찾아 빼내어 그 두 수를 더한다음
    new_num = dequeue() + dequeue()
    # 그 수를 total에 더해주고
    total += new_num
    # 다시 heap에 넣어준다.
    enqueue(new_num)

print(total)