# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        
        tmp = dummy
        
        while l and r:
            if l.val <= r.val:
                tmp.next = l
                
                tmp = tmp.next
                l = l.next
                
            else:
                tmp.next = r
                
                tmp = tmp.next
                r = r.next
                
        while l:
            tmp.next = l
            
            tmp = tmp.next 
            l = l.next
            
        while r:
            tmp.next = r
            
            tmp = tmp.next
            r = r.next
            
        return dummy.next
        