# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        
        tmp = dummy
        
        carry = 0
        
        while l1 and l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            sm = x+y+carry
            
            tmp.next = ListNode(sm%10)
            tmp = tmp.next
            
            carry = sm//10
            
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            x = l1.val
            sm = x+carry
            
            tmp.next = ListNode(sm%10)
            tmp = tmp.next
            
            carry = sm//10
            
            l1 = l1.next
            
        while l2:
            y = l2.val
            sm = y+carry
            
            tmp.next = ListNode(sm%10)
            tmp = tmp.next
            
            carry = sm//10
            
            l2 = l2.next
        
        if carry:
            tmp.next = ListNode(carry)
            tmp = tmp.next
            carry = 0
            
        return dummy.next