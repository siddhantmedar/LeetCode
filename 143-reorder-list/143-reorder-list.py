# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def merge(l,r):
            if not l:
                return r
            
            if not r:
                return l 
            
            dummy = ListNode(-101)
            dummy.next = head
            
            tmp = dummy
            
            while l and r:
                tmp.next = l
                tmp = tmp.next
                l = l.next
                
                tmp.next = r
                tmp = tmp.next
                r = r.next
                
            while l:
                tmp.next = l
                tmp = tmp.next
                l = l.next
                
            while r:
                tmp.next = r
                tmp = tmp.next
                r = r.next
                
            return dummy.next
        
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
            
            result = reverse2(head.next)
            
            head.next.next = head
            head.next = None
            
            return result
            
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
        
        return merge(left, right)
        