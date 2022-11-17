# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        def solve(right):
            nonlocal l,r,left,stop
            
            if l!=1:
                l-=1
                left = left.next
                
            if r!=1:
                r-=1
                solve(right.next)
                
            if left == right or right.next == left:
                stop = True
            
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next
            
        left = head
        stop = False
        
        solve(head)
        
        return head    
                
            