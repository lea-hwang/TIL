import sys
sys.stdin = open("1991_input.txt")

N = int(input())
tree = [[] for _ in range(N)]

for _ in range(N):
    # 부모, 왼쪽자식, 오른쪽 자식을 입력받아 숫자로 변환(A가 0)
    p, c1, c2 = map(lambda letter: ord(letter) - 65, sys.stdin.readline().rstrip().split())
    # [왼쪽자식, 오른쪽] 형태로 tree에 저장
    tree[p] = [c1 if c1 != -19 else None, c2 if c2 != -19 else None]

# 현재 -> 왼쪽 -> 오른쪽
def preorder(v):
    # 현재 방문
    print(chr(65+v), end='')
    # 왼쪽 방문
    if tree[v][0]: preorder(tree[v][0])
    # 오른쪽 방문
    if tree[v][1]: preorder(tree[v][1])

# 왼쪽 -> 현재 -> 오른쪽
def inorder(v):
    # 왼쪽 방문
    if tree[v][0]: inorder(tree[v][0])
    # 현재 방문
    print(chr(65+v), end='')
    # 오른쪽 방문
    if tree[v][1]: inorder(tree[v][1])

# 왼쪽 -> 오른쪽 -> 현재
def postorder(v):
    # 왼쪽 방문
    if tree[v][0]: postorder(tree[v][0])
    # 오른쪽 방문
    if tree[v][1]: postorder(tree[v][1])
    # 현재 방문
    print(chr(65 + v), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)
