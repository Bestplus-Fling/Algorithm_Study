import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


class Tree:
    def __init__(self):
        self.left = None
        self.right = None


def check_inorder():
    global tree, last_node
    stack = [[1, 0]]
    while stack:
        n, c = stack[-1]
        # left 확인
        if c == 0:
            if (left := tree[n].left) != -1:
                stack.append([left, 0])
                stack[-2][1] += 1
            else:
                stack[-1][1] += 1
        elif c == 1:
            last_node.append(n)
            if (right := tree[n].right) != -1:
                stack.append([right, 0])
                stack[-2][1] += 1
            else:
                stack[-1][1] += 1
        else:
            stack.pop()


def in_case():
    global tree, visited
    stack = [1]
    cnt = 0

    def mov(vtx):
        global visited
        nonlocal cnt, stack, node
        stack.append(vtx)
        cnt += 1
        visited.add((node, vtx))

    while stack:
        node = stack[-1]
        left = tree[node].left
        right = tree[node].right
        # tree[node].visited
        # 좌 우 노드에 방문 가능한지 확인
        if is_valid(node, left):
            mov(left)
            continue
        if is_valid(node, right):
            mov(right)
            continue
        if node == last_node[-1]:
            break
        stack.pop()
        cnt += 1
    return cnt


def is_valid(parent, vertex):
    global visited
    # -1이면 안가고
    # 이미 방문한 곳이여도 안가고
    if vertex == -1:
        return False
    elif (parent, vertex) in visited:
        return False
    return True

"""
정점 방문은 L -> Root -> R 순서
1. 최종적으로 방문하는 정점을 확인한다
2. 해당 정점으로까지 이동하는 횟수를 확인한다. 
"""
N = int(input())
tree = list(range(N+1))
visited = set()
for i in range(1, N+1):
    tree[i] = Tree()
for a, b, c in [list(map(int, input().split())) for _ in range(N)]:
    tree[a].left = b
    tree[a].right = c
# 1. 마지막 정점 확인
last_node = []
check_inorder()
print(in_case())
