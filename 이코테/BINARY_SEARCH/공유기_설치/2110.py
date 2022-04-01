import sys
sys.stdin = open('2110_input.txt', 'r')


N, C = map(int, input().split())                    # 집의 개수, 공유기의 개수
houses = [int(input()) for _ in range(N)]           # 집의 좌표
router = []
total = 0
# C개의 공유기를 N개의 집에 설치하여, 가장 인접한 두 공유기 사이의 거리를 최대로 하기.

# 1 2 4 8 9
# 제일 왼쪽과 제일 오른쪽에 설치.
# 남은 공유기를 가운데...에 설치?

houses.sort()

def installation(start, end):
    global total
    if total > 0: # 찾아야 하는 수가 남아 있다면,
        # 현재 start와 end를 기준으로 가장 중앙에 가까운 수를 찾는다.
        target = (houses[start] + houses[end])//2
        center = find_center(start, end, target)

        # 해당 숫자를 따로 저장한다. -> 홀수개일때만, 짝수개일 때는 저장 X.
        if total % 2:
            router.append(houses[center])
            total -= 1

        # 만약 남은 수가 있다면(3개 이상일 경우), 왼쪽과 오른쪽에서 동일한 개수의 숫자를 찾도록 재귀함수
        if total:
            #######################################
            # 만약 왼쪽에 충분한 개수의 숫자가 없을 때는 어떻게 처리..?
            installation(start, center, total//2)
            installation(center, end, total//2)


# 1 2 3 4 5 9 10
def find_center(start, end, target): # target과 가장 가까운 수를 찾는다.
    left, right = start, end
    while left <= right:
        mid = (left + right) // 2
        if houses[mid] == target:
            return mid
        elif houses[mid] > target:     # left side
            right = mid - 1
        else:
            left = mid + 1

    # 현재 mid를 중심으로 왼쪽 오른쪽 수를 찾고, 세 수와 target 사이의 차를 비교하여 제일 가까운 수 채택
    min_diff = houses[end] - houses[start]
    center = 0
    for i in range(mid-1, mid+2):
        if start <= i <= end:
            diff = abs(target - houses[i])
            if min_diff > diff:
                center = i
                min_diff = diff

    return center


router.extend([houses[0], houses[-1]]) # 제일 왼쪽과 제일 오른쪽 수를 넣음.
installation(0, N-1, C-2)

# router 순서대로 정렬
router.sort()
min_diff = houses[-1] - houses[0]
for i in range(len(router)-1):
    min_diff = min(min_diff, router[i+1] - router[i])

print(min_diff)

# 4
# 1 2 4 8 9
# 1 2 7 8 9 10 11 13
# 1 7 8 9 10
# 1 2 5 7 9




# 1 2 20 24 28 32 36 40