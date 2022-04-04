import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())  # 자연수의 개수, 뽑을 자연수의 개수, 연속해서 더해질 수 있는 횟수
nums = list(map(int, input().split()))

nums.sort(reverse=True)

first, second = nums[0], nums[1]  # 제일 큰 수 와 두번째로 큰 수

repeat = M // (K+1)
remain = M % (K+1)

total = first * (K * repeat + remain) + second * repeat
print(total)