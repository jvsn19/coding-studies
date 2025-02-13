from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        while list1 or list2:
            if list1 is None or (list2 is not None and list1.val >= list2.val):
                cur.next = list2
                list2 = list2.next
                cur = cur.next

            elif list2 is None or list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next

        cur.next = None
        return head.next