# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def solve(l,r):
            if not l:
                return r
            if not r:
                return l
            
            dummy = ListNode(-1000)
            ptr = dummy
            
            while l and r:
                if l.val<=r.val:
                    ptr.next = l
                    l = l.next
                    ptr = ptr.next
                else:
                    ptr.next = r
                    r = r.next
                    ptr = ptr.next
            
            while l:
                ptr.next = l
                l = l.next
                ptr = ptr.next
            
            while r:
                ptr.next = r
                r = r.next
                ptr = ptr.next
                
            return dummy.next
        
        
        return solve(list1,list2)