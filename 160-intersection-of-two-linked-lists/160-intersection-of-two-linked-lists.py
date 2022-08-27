# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(head):
            count = 0
            
            while head:
                count+=1
                head = head.next
                
            return count
        
        c1, c2 = length(headA), length(headB)
        
        
        if c1 > c2:
            k = c1-c2
            while k != 0:
                headA = headA.next
                k-=1
            
        elif c1 < c2:
            k = c2-c1
            while k != 0:
                headB = headB.next
                k-=1
        
        while headA and headB:
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
            
        return None