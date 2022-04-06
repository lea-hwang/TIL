import sys
sys.stdin = open('input.txt', 'r')


def enqueue(N):
    global len_arr
    arr.append(N)
    len_arr += 1
    c = len_arr - 1
    p = c//2
    while p > 0 and (abs(arr[p]) > abs(arr[c]) or (abs(arr[p]) == abs(arr[c]) and arr[p] > arr[c])):
        arr[p], arr[c] = arr[c], arr[p]
        c = p
        p = c // 2

def dequeue():
    global len_arr
    if len_arr == 1:
        print(0)
    elif len_arr == 2:
        len_arr -= 1
        print(arr.pop())
    else:
        print(arr[1])
        arr[1] = arr.pop()
        len_arr -= 1
        p = 1
        c = p*2
        while len_arr - 1 >= c:
            if len_arr - 1 >= c+1: # 오른쪽 노드가 존재할 때
                # 둘 중에 작은 수를 찾아서 c에 저장
                if abs(arr[c]) > abs(arr[c+1]) or (abs(arr[c]) == abs(arr[c+1]) and arr[c] > arr[c+1]):
                    c += 1
            # 부모 노드와 비교
            if abs(arr[c]) < abs(arr[p]) or (abs(arr[c]) == abs(arr[p]) and arr[c] < arr[p]):
                arr[c], arr[p] = arr[p], arr[c]
                p = c
                c = p*2
            else:
                break


N = int(input())
arr = [0]
len_arr = 1
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        enqueue(num)
    else:
        dequeue()