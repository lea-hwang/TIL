import sys
sys.stdin = open('1107_input.txt', 'r')

N = input()  # 이동하려는 채널
N_list = list(map(int, N))
M = int(input())  # 고장난 버튼의 개수
if M:
    btn_list = list(map(int, input().split()))
else:
    btn_list = []


def check(num):  # 해당 숫자가 가능한지 여부 확인
    if num < 0: return False
    num_list = [num % 10]
    while num > 0:
        num_list.append(num % 10)
        num //= 10
    if set(num_list) & set(btn_list):
        return False
    else:
        return True


def len_num(N):
    i = 1
    while N >= 10:
        N //= 10
        i += 1
    return i


def find_number(N):
    num = int(N)
    i = 0
    while True:
        if check(num - i):
            return i + len_num(num - i)
        elif check(num + i):
            return i + len_num(num + i)
        i += 1


# 만약 현재 수에 누를 수 없는 버튼이 있다면..
if set(N_list) & set(btn_list):
    min_v = min(abs(int(N) - 100), find_number(N))
    print(min_v)
else:
    print(len(N))
