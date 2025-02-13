# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def get_mid(node):
            slow = fast = node
            size = 1

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                size += 2

            if fast.next is not None:
                size += 1

            return slow, slow.next, size & 1


        def reverse(node):
            prev = None

            while node:
                node.next, node, prev = prev, node.next, node


        def compare(node_a, node_b):
            while node_a and node_b:
                if not node_a or not node_b or node_a.val != node_b.val:
                    return False

                node_a = node_a.next
                node_b = node_b.next

            return True


        if head is None:
            return True

        fst, sec, is_odd = get_mid(head)
        fst.next = None
        reverse(head)

        if is_odd:
            fst = fst.next

        return compare(fst, sec)