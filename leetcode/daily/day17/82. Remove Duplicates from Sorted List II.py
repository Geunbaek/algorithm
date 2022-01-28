# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node, ret):
            if not node:
                return
            if node.val in ban:
                dfs(node.next, ret)
            elif node.next and node.val == node.next.val:
                ban.add(node.val)
                dfs(node.next.next, ret)
            else:
                if -100 <= ret.val <= 100:
                    ret.next = ListNode(node.val)
                    dfs(node.next, ret.next)
                else:
                    ret.val = node.val
                    dfs(node.next, ret)

        ban = set()
        ans = ListNode(-101)
        dfs(head, ans)

        if ans.val == -101:
            return None
        return ans







