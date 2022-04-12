import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

class TreeNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def inorder_traversal(node):
    if node not in tree: return
    inorder_traversal(tree[node].left)
    inorder.append(node)
    inorder_traversal(tree[node].right)

def similar_inorder(node):
    if node == -1: return

    if not s_order:
        s_order.append(node)
    elif s_order[-1] != node:
        s_order.append(node)

    similar_inorder(tree[node].left)

    if not s_order:
        s_order.append(node)
    elif s_order[-1] != node:
        s_order.append(node)

    similar_inorder(tree[node].right)

    if not s_order:
        s_order.append(node)
    elif s_order[-1] != node:
        s_order.append(node)

n = int(input())
tree = {}
inorder = []

for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a] = TreeNode(b, c)

inorder_traversal(1)
final = inorder[-1]
s_order = []
visited = [0 for _ in range(n + 1)]
similar_inorder(1)

left = 1
right = len(s_order) - 1
while True:
    if s_order[right] != final:
        right -= 1
    else:
        break
print(len(s_order[left: right + 1]))