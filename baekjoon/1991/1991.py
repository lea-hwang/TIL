import sys
sys.stdin = open('1991_input.txt', 'r')

N = int(input())
nodes = {}
for i in range(N):
    p, c1, c2 = input().split()
    nodes[p] = [c1, c2]

def preorder(v):
    if v != '.':
        print(v, end='')
        preorder(nodes[v][0])
        preorder(nodes[v][1])

def inorder(v):
    if v != '.':
        inorder(nodes[v][0])
        print(v, end='')
        inorder(nodes[v][1])

def postorder(v):
    if v != '.':
        postorder(nodes[v][0])
        postorder(nodes[v][1])
        print(v, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
