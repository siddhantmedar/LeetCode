# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head
        
        while curr:
            ref = curr.next
            
            curr.next = pre
            pre = curr
            curr = ref
            
        return pre
        