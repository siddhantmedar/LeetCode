# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1000)
        dummy.next = head
        
        slow,fast = dummy, dummy.next
        
        while k:
            fast = fast.next
            k-=1
            
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next if slow.next.next else None
        
        return dummy.next