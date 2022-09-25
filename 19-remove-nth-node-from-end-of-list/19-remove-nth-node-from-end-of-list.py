# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], K: int) -> Optional[ListNode]:
        # N-K+1 from the front
        N = 0
        tmp = head
        
        while tmp:
            N+=1
            
            tmp = tmp.next
            
        dummy = ListNode(-1)
        dummy.next = head
        
        pre, curr = dummy, dummy.next
        
        count = N-K+1
        
        while count != 1:
            pre = pre.next
            curr = curr.next
            
            count-=1
        
        pre.next = curr.next if curr else None
        
        return dummy.next