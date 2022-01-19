# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = []
        node = head
        while node:
            temp.append(node.val)
            node = node.next

        count = len(temp) - n

        if count == 0:
            head = head.next
            return head

        node = head
        index = 0
        while node:
            if count - 1 == index:
                node.next = node.next.next
            node = node.next
            index += 1
        return head