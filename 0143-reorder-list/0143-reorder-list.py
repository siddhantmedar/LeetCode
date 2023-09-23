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
            
            dummy = ListNode(-1000)
            ptr = dummy
            
            while l and r:
                if l.val<=r.val:
                    ptr.next = l
                    l = l.next
                    ptr = ptr.next
                else:
                    ptr.next = r
                    r = r.next
                    ptr = ptr.next
            
            while l:
                ptr.next = l
                l = l.next
                ptr = ptr.next
            
            while r:
                ptr.next = r
                r = r.next
                ptr = ptr.next
                
            return dummy.next
        
        
        def reverse(head):
            if not head or not head.next:
                return head
            
            res = reverse(head.next)
            
            head.next.next = head
            head.next = None
            
            return res
        
        def mid(head):
            slow, fast = head, head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        
        pre = mid(head)
        
        rev = pre.next
        head2 = pre.next
        pre.next = None
        
        head1 = head
        head2 = reverse(head2)
        
        dummy = ListNode(-1)
        ptr = dummy
        
        while head1 and head2:
            ptr.next = head1
            head1 = head1.next
            ptr = ptr.next
            
            ptr.next = head2
            head2 = head2.next
            ptr = ptr.next
            
        while head1 and head2:
            ptr.next = head1
            head1 = head1.next
            ptr = ptr.next
            
            ptr.next = head2
            head2 = head2.next
            ptr = ptr.next
        
        while head1:
            ptr.next = head1
            head1 = head1.next
            ptr = ptr.next
            
        while head2:
            ptr.next = head2
            head2 = head2.next
            ptr = ptr.next
            
        while head and head.next:
            head = head.next
        
        # head.next = reverse(rev)
        
        return dummy.next
        