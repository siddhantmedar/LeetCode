# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            count = 0
            
            while head:
                count+=1
                
                head = head.next
                
            return count
        
        
        def solve(right, pre=None):
            nonlocal left, stop, result
            
            if not right:
                return
            
            solve(right.next, right)
            
            if not stop:
                if left!=right:
                    right.next = left
                    pre.next = None
                    result = right
                    stop = True
        
        if not head:
            return head
        
        N = length(head)
        K = k%N
        
        result = head
        left = None
        
        while K:
            stop = False
            left = result
            solve(result)
            K-=1
            
        return result