import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    print(node.data, end = "")
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.data, end="")
    if node.right:
        inorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.data, end="")

n = int(input())
tree = {chr(ord('A')+i) : Node(chr(ord('A')+i)) for i in range(n)}


for _ in range(n):
    a, b, c = input().strip().split()
    if b != '.':
        tree[a].left = tree[b]
    if c != '.':
        tree[a].right = tree[c]

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
