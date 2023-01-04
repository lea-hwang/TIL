import sys
sys.stdin = open("input.txt")

# 같은 방식을 class 없이 구현..?
lines = sys.stdin.readlines()

N = len(lines)