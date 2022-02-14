from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compared(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and not node2:
                return False
            elif not node1 and node2:
                return False

            if node1.val != node2.val:
                return False

            return compared(node1.left, node2.left) and compared(node1.right, node2.right)

        def dfs(node1, node2):
            if not node1:
                return

            if node1.val == node2.val and compared(node1, node2):
                return True

            return dfs(node1.left, node2) or dfs(node1.right, node2)

        return dfs(root, subRoot)








sol = Solution()
sol.isSubtree(TreeNode(1), TreeNode(0))