# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse1(head):
            pre, curr = None, head
            
            while curr:
                ref = curr.next
                curr.next = pre
                pre = curr
                curr = ref
                
            return pre
            
        def reverse2(head):
            if not head or not head.next:
                return head
            
            res = reverse2(head.next)
            
            head.next.next = head
            head.next = None
            
            return res
        
        def middle(head):
            slow, fast = head, head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        
        mid = middle(head)
        
        left = head
        right = mid.next
        mid.next = None
        right = reverse2(right)
        
        ptr1, ptr2 = left, right
        
        result = None
        
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                result = False
                break
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        if result == None:
            result = True
        
        while left.next:
            left = left.next
            
        left.next = reverse2(right)
        
        return result
        
        
        
        