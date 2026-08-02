from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: nothing to reverse
        if not head or left == right:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        # Step 1: move prev to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: reverse sublist
        curr = prev.next
        for _ in range(right - left):
            next_ptr = curr.next
            curr.next = next_ptr.next
            next_ptr.next = prev.next
            prev.next = next_ptr

        return dummy.next
