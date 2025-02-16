from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(next = head)
        n_ahead = head

        for _ in range(n):
            n_ahead = n_ahead.next

        prev, cur = new_head, head

        while n_ahead:
            n_ahead = n_ahead.next
            prev = prev.next
            cur = cur.next

        prev.next = cur.next
        return new_head.next