# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []

        node = head
        while node:
            temp.append(node.val)
            node = node.next
        ret_node = ListNode(temp[len(temp) // 2])
        node = ret_node

        for i in temp[(len(temp) // 2) + 1:]:
            node.next = ListNode(i)
            node = node.next
        return ret_node