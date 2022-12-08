import sys
from itertools import combinations

sys.stdin = open("input.txt")


while True:
    line = sys.stdin.readline().rstrip()
    if line =='0': break

    line = line.split()
    for case in list(combinations(line[1:], 6)):
        print(*case)
    print()