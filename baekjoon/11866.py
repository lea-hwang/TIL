import sys
sys.stdin = open('11866_input.txt', 'r')

N, K = map(int, input().split())
nums = [i for i in range(1, N+1)]
josephus = []
while N > 0:
    josephus += [nums[(K-1)%N]]
    nums = nums[(K-1)%N+1:] + nums[:(K-1)%N]
    N -= 1

josephus += nums
print(f'<{", ".join(list(map(str,josephus)))}>')
