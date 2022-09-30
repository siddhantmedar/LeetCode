# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middle(head):
            slow = head
            fast = head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        def reverse(head):
            if not head or not head.next:
                return head
            
            result = reverse(head.next)
            
            head.next.next = head
            head.next = None
            
            return result
        
        mid = middle(head)
        
        rev = reverse(mid.next)
        
        mid.next = rev
        
        ptr1, ptr2 = head, mid.next
        
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return True