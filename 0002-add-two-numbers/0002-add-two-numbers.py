# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = ListNode(-1000)
        dummy = ptr
        
        carry = 0
        
        while l1 and l2:
            total = l1.val + l2.val + carry
            dummy.next = ListNode(total%10)
            carry = total//10
            
            l1 = l1.next
            l2 = l2.next
            
            dummy = dummy.next
            
        
        while l1:
            total = l1.val+carry
            dummy.next = ListNode(total%10)
            carry = total//10
            
            l1 = l1.next
            dummy = dummy.next
        
        while l2:
            total = l2.val+carry
            dummy.next = ListNode(total%10)
            carry = total//10
            
            l2 = l2.next
            dummy = dummy.next
        
        if carry:
            dummy.next = ListNode(carry)
        return ptr.next