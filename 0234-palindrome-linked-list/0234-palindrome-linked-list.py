# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def rev(head):
            if not head or not head.next:
                return head
            
            res = rev(head.next)
            
            head.next.next = head
            head.next = None
            
            return res
            
        
        def mid(head):
            slow, fast = head, head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        m = mid(head)
        p2 = m.next
        p2 = rev(p2)
        
        m.next = p2
        
        p1 = head
        
        while p1 and p2:
            if p1.val != p2.val:
                return False
            
            p1 = p1.next
            p2 = p2.next
            
        return True
        
        