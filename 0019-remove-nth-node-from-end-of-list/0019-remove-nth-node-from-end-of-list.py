# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            cnt = 0
            
            while head:
                cnt+=1
                head = head.next
                
            return cnt
        
        
        dummy = ListNode(-1)
        dummy.next = head
        
        pre, curr = dummy, head
        n = length(head)
        
        for _ in range(n-k):
            pre = pre.next
            curr = curr.next
            
        pre.next = curr.next
        
        return dummy.next