# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        
        dummy.next = head
        
        pre, curr = dummy, dummy.next
        
        while curr:
            if pre.val != curr.val:
                pre = pre.next
                curr = curr.next
                
            else:
                pre.next = curr.next
                curr = curr.next
                
        return dummy.next