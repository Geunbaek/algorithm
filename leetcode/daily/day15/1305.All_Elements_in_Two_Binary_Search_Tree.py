# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ret = []

        def preorder(node):
            if node:
                if node.left:
                    preorder(node.left)
                ret.append(node.val)
                if node.right:
                    preorder(node.right)
        preorder(root1)
        preorder(root2)
        ret.sort()
        return ret