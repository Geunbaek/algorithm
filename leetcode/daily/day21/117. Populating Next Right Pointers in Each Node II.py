# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        temp = {}

        def dfs(node, depth):

            temp[depth] = temp.get(depth, []) + [node]
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 0)

        def oper(node, depth):

            idx = temp[depth].index(node)

            if idx != len(temp[depth]) - 1:
                node.next = temp[depth][idx + 1]
            if node.left:
                oper(node.left, depth + 1)
            if node.right:
                oper(node.right, depth + 1)

        oper(root, 0)

        return root
sol = Solution()
sol.connect(Node(1, Node(2, Node(4), Node(5)), Node(3,None, Node(7))))
sol.connect(Node(0))