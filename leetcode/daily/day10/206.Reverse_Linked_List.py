# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        node = ListNode(ret.pop())
        head = node
        while ret:
            node.next = ListNode(ret.pop())
            node = node.next
        return head
