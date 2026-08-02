# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        
        while(curr!=None):
            #assign next_ptr
            next_ptr= curr.next

            #move link to previous
            curr.next= prev

            #update

            prev= curr
            curr=next_ptr
        
        #update head of reversed linked list
        head=prev    
        return prev



        