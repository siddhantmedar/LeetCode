# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        head1, head2 = head, head.next
        
        tmp = head
        
        while tmp:
            ref = tmp.next
            
            tmp.next = tmp.next.next if tmp.next else None
            
            tmp = ref
            
        while head1.next:
            head1 = head1.next
            
        head1.next = head2
        
        return head