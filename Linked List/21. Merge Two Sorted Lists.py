# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        m = ListNode()
        dummy_head = m
        p = list1
        q = list2
        while p and q:
            if p.val < q.val:
                m.next = p
                p = p.next
            else:
                m.next = q
                q = q.next
            m = m.next
        if q:
            m.next = q
        if p:
            m.next = p
        return dummy_head.next