# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def solve(head):
            nonlocal p, res
            
            if not head:
                return
            
            solve(head.next)
            
            res+=(head.val*(2**p))
            p+=1
            
            
            
        p = 0
        res = 0
        
        solve(head)
        
        return res
        