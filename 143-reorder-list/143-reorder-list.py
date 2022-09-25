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

        def middle(head):
            slow, fast = head, head.next
            
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
        
        def merge(l,r):
            if not l:
                return r
            
            if not r:
                return l
            
            dummy = ListNode(-1)
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
            
            
        mid = middle(head)

        l = head
        r = mid.next
        
        mid.next = None
        
        rev = reverse(r)
        
        return merge(l, rev)