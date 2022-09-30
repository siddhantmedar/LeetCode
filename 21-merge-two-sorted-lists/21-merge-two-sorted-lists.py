# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        
        tmp = dummy
        
        while l and r:
            if l.val <= r.val:
                tmp.next = l
                l = l.next
                tmp = tmp.next
                
            else:
                tmp.next = r
                r = r.next
                tmp = tmp.next
                
        while l:
            tmp.next = l
            l = l.next
            tmp = tmp.next
            
        while r:
            tmp.next = r
            r = r.next
            tmp = tmp.next
            
        return dummy.next