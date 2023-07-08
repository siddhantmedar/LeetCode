# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('inf'))
        dummy.next = head
        
        pre = dummy
        curr = dummy.next
        
        while curr:
            ref = curr.next
            if curr.val == pre.val:
                pre.next = ref
            else:        
                pre = curr
                
            curr = ref

            
        return dummy.next