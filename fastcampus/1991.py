import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for _ in range(n):
    root, left, right = map(str, input().split())
    graph[root].append(left)
    graph[root].append(right)

def preorder(node):
    if node != '.':
        print(node, end = '')
        preorder(graph[node][0])
        preorder(graph[node][1])

def inorder(node):
    if node != '.':
        inorder(graph[node][0])
        print(node, end='')
        inorder(graph[node][1])

def postorder(node):
    if node != '.':
        postorder(graph[node][0])
        postorder(graph[node][1])
        print(node, end='')

preorder('A')
print()
inorder("A")
print()
postorder("A")