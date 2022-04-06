import sys
sys.stdin = open('input.txt', 'r')

my_set = set()

orders = {
    'add': lambda x: my_set.add(x),
    'check':lambda x: print(1) if x in my_set else print(0),
    'remove':lambda x: my_set.discard(x),
    'toggle':lambda x: my_set.remove(x) if x in my_set else my_set.add(x),
}



M = int(input())
for i in range(M):
    line = input().split()
    if len(line) == 2:
        order, num = line[0], int(line[1])
        orders[order](num)
    else:
        if line[0] == "all":
            my_set.update({i for i in range(1, 21)})
        else:
            my_set.clear()
