# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1, c2 = headA, headB
        
        while c1 != c2:
            c1 = c1.next if c1 else headB
            c2 = c2.next if c2 else headA
            
        return c1