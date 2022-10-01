# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            count = 0
            
            while head:
                count+=1
            
                head = head.next
                
            return count
        
        
        n = length(head)
        pos = n-k+1
        
        dummy = ListNode(-101)
        dummy.next = head
    
        pre, curr = dummy, head
        
        while curr:
            pos-=1
            
            if pos == 0:
                pre.next = curr.next
                break
                
            pre = pre.next
            curr = curr.next
                
        return dummy.next