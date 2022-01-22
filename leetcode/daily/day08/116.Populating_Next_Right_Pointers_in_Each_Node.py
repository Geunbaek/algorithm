from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        graph = {}

        def dfs(node, depth):
            if depth not in graph:
                graph[depth] = []
            graph[depth].append(node.val)
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        dfs(root, 0)
        def oper(node, depth):
            if graph[depth].index(node.val) == len(graph[depth]) -1:
                node.next = None
            else:
                node.next = graph[depth].index(node.val) + 1
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        oper(root, 0)
        return root


