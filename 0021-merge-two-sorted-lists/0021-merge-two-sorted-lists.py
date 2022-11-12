# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l,r):
            if not l:
                return r
            
            if not r:
                return l
            
            dummy = ListNode(-1)
            tmp = dummy
            
            while l and r:
                if l.val <= r.val:
                    dummy.next = l
                    l = l.next
                    dummy = dummy.next
                    
                elif l.val > r.val:
                    dummy.next = r
                    r = r.next
                    dummy = dummy.next
                    
                    
            while l:
                dummy.next = l
                l = l.next
                dummy = dummy.next
                
            while r:
                dummy.next = r
                r = r.next 
                dummy = dummy.next
                
            return tmp.next
        
        return merge(list1, list2)