food_times = [1,2,3]
k = 5

# 각 횟수별로 사라지는 음식의 인덱스를 정리.

# 방송이 몇번째일 때 중단되었는지.? -
# 1 라운드 -> 1의 개수만큼 삭제됨
# 2 라운드 -> 2의 개수만큼 삭제됨

def solution(food_times, k):
    times = {}
    foods = len(food_times)
    for time in food_times:
        if times.get(time, 0):
            times[time] += 1
        else:
            times[time] = 1

    # 몇 시간까지 가는지 체크
    # 남은 음식이 없을때
    t = 1
    remain_food = foods
    while k >= remain_food > 0: # k는 남은 시간 foods 남은 음식의 수
        k -= remain_food
        remain_food -= times.get(t, 0) # 없는 시간이 있을 수 있기 때문에 get 사용
        t += 1

    # 만약 남아있는 음식이 없는 거라면 return -1
    if remain_food <= 0 and k >= 0:
        return -1

    # 현재 t 이상인 음식들만 남아있는 상황
    cnt = 0
    for i in range(foods):
        if food_times[i] >= t:
            cnt += 1
            if cnt == k+1:
                return i+1

print(solution(food_times, k))

# 시간초과 수정필요


