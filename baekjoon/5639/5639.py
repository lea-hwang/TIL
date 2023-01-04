# 시간초과(2시간 동안 풀었는데..)
# 전위 순회(루트 왼쪽 오른쪽)
# 후위 순회(왼쪽 오른쪽 루트)
# 전위 순회한 결과물이 주어졌을 때 후위순회한 결과물.

# 1. 전위 순회를 이용해서 트리 만들기
# 현재 들어온 값이 현재의 값보다 작으면 왼쪽에 넣기
# 현재 들어온 값이 (현재의 값보다 크고)
#   부모의 값보다 작으면 현재노드의 오른쪽에 넣기
#   부모의 값보다 크면 부모노드의 오른쪽에 넣기

import sys

class Node:
    def __init__(self, value):
        self.value = value      # 노드의 값
        self.left = None        # left child node
        self.right = None       # right child node
        self.parent = None      # parent node
        self.visited = False    # 방문여부

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent

    def print_node(self):
        print(f"value: {self.value}, "
              f"left: {self.left.value if self.left else None}, "
              f"right:{self.right.value if self.right else None}"
        )


sys.stdin = open("input.txt")
# 모든 입력 미리 받기
lines = sys.stdin.readlines()

# 루트 노드 생성
root = Node(int(lines[0].rstrip()))
cur_node = root
for line in lines[1:]:
    num = int(line.rstrip())

    next_node = Node(num)
    # 숫자가 현재 노드의 숫자보다 작으면 현재 노드의 왼쪽에 넣기
    if num < cur_node.value:
        cur_node.set_left(next_node)
        next_node.set_parent(cur_node)
    # 숫자가 현재 노드의 숫자보다 크면
    else:
        # 오른쪽에 넣을 수 있게 부모노드를 탐색하면서 cur_node 찾기(부모노드가 존재하지 않다면 stop)
        parent_stack = [cur_node]
        while cur_node.parent and num > cur_node.parent.value:
            cur_node = cur_node.parent
            # 오른쪽이 비어있지 않은 부모만 stack에 넣어줌
            if not cur_node.right:
                parent_stack.append(cur_node)
        # 가장 마지막 부모를 cur_node로 지정
        cur_node = parent_stack[-1]
        # 현재 노드의 오른쪽 노드로 지정
        cur_node.set_right(next_node)
        next_node.set_parent(cur_node)
    # 현재 노드를 다음 노드로 지정
    cur_node = next_node


# 후위 순회하기(preorder)
# 루트 노드를 시작으로 왼 - 오 - 루트 순으로 탐색
# 방문 순서를 stack으로 구현
# 1. 왼쪽 노드가 있고 방문한 적이 없다면 왼쪽 노드 이동
# 2. 오른쪽 노드가 있고 방문한 적이 없다면 오른쪽 노드 이동
# 3. 왼쪽 오른쪽 둘다 방문했다면 현재 노드 방문
def preorder(root):
    # 방문한 노드 리스트
    stack = []
    stack.append(root)
    while stack:
        C = stack[-1]
        # 왼쪽 노드가 있고 방문한 적이 없다면 왼쪽 노드로 이동
        if C.left and not C.left.visited:
            stack.append(C.left)
            continue
        # 오른쪽 노드가 있고 방문한 적이 없다면 오른쪽 노드로 이동
        if C.right and not C.right.visited:
            stack.append(C.right)
            continue

        # 현재 노드 방문
        C.visited = True
        print(C.value)
        stack.pop()

preorder(root)
