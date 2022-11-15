# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        first, second = dummy, dummy
        
        while k:
            first = first.next
            k-=1
            
        while first.next:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        
        return dummy.next