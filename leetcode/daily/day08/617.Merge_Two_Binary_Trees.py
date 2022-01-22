# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        head = TreeNode(root1.val + root2.val)

        def dfs(r1, r2, node):
            if r1 and r2 and r1.left and r2.left:
                node.left = TreeNode(r1.left.val + r2.left.val)
                dfs(r1.left, r2.left, node.left)
            elif r1 and r1.left:
                node.left = TreeNode(r1.left.val)
                dfs(r1.left, None, node.left)
            elif r2 and r2.left:
                node.left = TreeNode(r2.left.val)
                dfs(None, r2.left, node.left)

            if r1 and r2 and r1.right and r2.right:
                node.right = TreeNode(r1.right.val + r2.right.val)
                dfs(r1.right, r2.right, node.right)
            elif r1 and r1.right:
                node.right = TreeNode(r1.right.val)
                dfs(r1.right, None, node.right)
            elif r2 and r2.right:
                node.right = TreeNode(r2.right.val)
                dfs(None, r2.right, node.right)

        dfs(root1, root2, head)
        return head

sol = Solution()
sol.mergeTrees(TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)), TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7))))