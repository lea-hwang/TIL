import sys
sys.stdin = open('1427_input.txt', 'r')

nums = list(map(int, input()))
nums.sort(reverse=True)
print(''.join(map(str, nums)))