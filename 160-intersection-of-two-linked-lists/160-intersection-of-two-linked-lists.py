# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cheadA, cheadB = headA, headB

        while cheadA != cheadB:
            cheadA = cheadA.next if cheadA else headB
            cheadB = cheadB.next if cheadB else headA
        return cheadA