# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        
        dummy.next = head
        
        pre, curr = dummy, dummy.next
        
        while curr:
            if curr.val != val:
                pre = curr
                curr = curr.next
                
            else:
                pre.next = curr.next
                curr = curr.next
                
        return dummy.next
        