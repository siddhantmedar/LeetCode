# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, p: ListNode, q: ListNode) -> Optional[ListNode]:
        st = set()
        
        while p:
            st.add(p)
            
            p = p.next
            
        while q:
            if q in st:
                return q
            
            q = q.next
            
        return None