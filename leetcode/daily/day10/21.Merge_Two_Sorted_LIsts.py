# Definition for singly-linked list.


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        def dfs(node, l, r):
            if l and r:
                if l.val <= r.val:
                    node.next = ListNode(l.val)
                    dfs(node.next, l.next, r)
                else:
                    node.next = ListNode(r.val)
                    dfs(node.next, l, r.next)
            elif l:
                node.next = ListNode(l.val)
                dfs(node.next, l.next, r)
            else:
                node.next = ListNode(r.val)
                dfs(node.next, l, r.next)

        if list1.val <= list2.val:
            head = ListNode(list1.val)
            dfs(head, list1.next, list2)
        else:
            head = ListNode(list2.val)
            dfs(head, list1, list2.next)

        return head