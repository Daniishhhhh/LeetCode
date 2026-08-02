
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True   # Single node or empty list is always palindrome

        # Step 1: Find middle using slow/fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half starting from slow
        prev = None
        curr = slow
        while curr:
            next_ptr = curr.next
            curr.next = prev
            #update
            prev = curr
            curr = next_ptr
        # Now 'prev' is head of reversed second half

        # Step 3: Compare first half and reversed second half
        first_half = head
        second_half = prev
        while second_half:   # only need to check second half length
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
