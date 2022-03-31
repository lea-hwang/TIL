import sys
sys.stdin = open('input.txt', 'r')

N, X = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
# X의 개수 세기

def binary_search(start, end, target):
    global cnt
    if start <= end:
        mid = (start + end) // 2
        # 만약 x를 만나면, 카운트 + 1, 좌우 모두 바이너리 서치 실행
        if arr[mid] == target:
            cnt += 1
            binary_search(start, mid-1, target)
            binary_search(mid+1, end, target)
        elif arr[mid] < target:
            binary_search(mid+1, end, target)
        else:
            binary_search(start, mid-1, target)


binary_search(0, N-1, X)

if cnt: print(cnt)
else: print(-1)