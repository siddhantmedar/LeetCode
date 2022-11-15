# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l,r):
            if not l:
                return r
            
            if not r:
                return l
            
            dummy = ListNode(-1)
            tmp = dummy
            
            while l and r:
                if l.val <= r.val:
                    tmp.next = l
                    l = l.next
                
                else:
                    tmp.next = r
                    r = r.next
                
                tmp = tmp.next
                
            while l:
                tmp.next = l
                l = l.next
                tmp = tmp.next
                
            while r:
                tmp.next = r
                r = r.next
                tmp = tmp.next
                    
            return dummy.next
            
            
        def middle(head):
            slow, fast = head, head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        def mergeSort(head):
            if not head or not head.next:
                return head
            
            mid = middle(head)
            
            left=  head
            right = mid.next
            
            mid.next = None
            
            l = mergeSort(left)
            r = mergeSort(right)
            
            return merge(l, r)
        
        
        return mergeSort(head)