import sys
sys.stdin = open("input.txt")

A, B, C = map(int, input().split())


def get_remain(a, b):
    if b == 1:
        return a % C
    else:
        tmp = get_remain(a, b//2)
        if b % 2:
            return (tmp * tmp * a) % C
        else:
            return (tmp * tmp) % C

print(get_remain(A, B))