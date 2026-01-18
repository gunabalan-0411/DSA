"""
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        cur = head
        while cur.next:
            new_node = ListNode(gcd(cur.val, cur.next.val))
            temp = cur.next
            cur.next = new_node
            new_node.next = temp

            cur = temp

        return head
