# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-100000)
        dummy.next = head
        
        pre, curr = dummy, head
        
        while curr:
            if pre.val != curr.val:
                curr = curr.next
                pre = pre.next
                
            else:
                pre.next = curr.next
                curr = curr.next
                
        return dummy.next