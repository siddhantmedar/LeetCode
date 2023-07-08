# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1,l2):
            if not l1:
                return l2
            
            if not l2:
                return l1
            
            dummy = ListNode(float('inf'))
            ptr = dummy
            
            p1, p2 = l1,l2
            
            while p1 and p2:
                if p1.val <= p2.val:
                    ptr.next = p1
                    p1 = p1.next
                    ptr = ptr.next
                    
                else:
                    ptr.next = p2
                    p2 = p2.next
                    ptr = ptr.next
                    
            while p1:
                ptr.next = p1
                p1 = p1.next
                ptr = ptr.next
                
            while p2:
                ptr.next = p2
                p2 = p2.next
                ptr = ptr.next
                
            return dummy.next
        
        return merge(list1, list2)