# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        tmp = deque()
        
        while head:
            tmp.appendleft(head.val)
            head = head.next
            
        p = 0
        res = 0
        
        for ele in tmp:
            res+=ele*(2**p)
            p+=1
        
        return res