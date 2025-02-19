from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for idx, head in enumerate(lists):
            if head is None:
                continue
            
            heapq.heappush(heap, (head.val, idx))

        new_head = ListNode()
        cur = new_head

        while heap:
            _, idx = heapq.heappop(heap)
            node = lists[idx]

            if node.next:
                heapq.heappush(heap, (node.next.val, idx))

            cur.next = node
            cur = cur.next
            lists[idx] = lists[idx].next

        return new_head.next