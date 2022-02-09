import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스의 수
T = int(input())
# foreign number
f_nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(T):
    # case 번호, 숫자열 길이
    case, length = input().strip('#').split()
    # foreign string 받기
    f_str = input()
    new_f_str = ''
    # 2.
    for i in range(10):
        # 1. 각 숫자 별로 몇 개씩 있는지 센다.
        count = f_str.count(f_nums[i])
        # 2. 그 수만큼 문자열을 만들어 새로운 문자열에 이어붙인다.
        if new_f_str != '' and count:
            new_f_str += ' '
        new_f_str += ' '.join([f_nums[i]] * count)
    print(f'#{case}')
    print(new_f_str)