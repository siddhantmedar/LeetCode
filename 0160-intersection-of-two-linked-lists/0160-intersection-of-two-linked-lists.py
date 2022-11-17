# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, p: ListNode, q: ListNode) -> Optional[ListNode]:
        ptr1,ptr2 = p,q
        
        while ptr1!=ptr2:
            ptr1 = ptr1.next if ptr1 else q
            ptr2 = ptr2.next if ptr2 else p
            
        return ptr1