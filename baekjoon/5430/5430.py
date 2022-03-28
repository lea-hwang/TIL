import sys
sys.stdin = open('5430_input.txt', 'r')

T = int(input())
for _ in range(T):
    p = input()                                     # 실행할 함수
    n = int(input())                                # 숫자의 개수
    nums = list(input().strip('[]').split(','))     # 숫자
    is_reversed = False                             # 뒤집혀있는지 여부 확인
    start = 0
    end = n-1

    # 만약 D 명령이 숫자 개수보다 많을 경우 에러 발생
    D_num = p.count('D')
    if D_num > n:
        print('error')
        continue


    # 각 명령에 대하여 실행
    for order in p:
        # 뒤집기 명령
        if order == "R":
            is_reversed = not is_reversed

        # 삭제 명령
        else:
            if is_reversed:             # 뒤집혀있을 경우
                end -= 1                # 뒤쪽에서 하나 제거
            else:                       # 뒤집혀 있지 않을 경우
                start += 1              # 앞쪽에서 하나 제거


    # 출력
    new_num = list(map(str, nums[start:end+1])) # 해당 배열 저장

    if is_reversed:                             # 만약 뒤집혀 있다면 뒤집기
        new_num.reverse()

    print("[" + ','.join(new_num) + "]")


