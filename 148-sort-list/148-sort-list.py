# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(head):
            slow, fast = head, head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        def merge(l,r):
            if not l:
                return r
            
            if not r:
                return l
            
            dummy = ListNode(-101)
            tmp = dummy
            
            while l and r:
                if l.val <= r.val:
                    tmp.next = l
                    tmp = tmp.next
                    l = l.next
            
                else:
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
        
        def mergeSort(head):
            if not head or not head.next:
                return head
            
            mid = middle(head)
        
            p = head
            q = mid.next
            
            mid.next = None
            
            left = mergeSort(p)
            right = mergeSort(q)
            
            result = merge(left, right)
            
            return result
        
        return mergeSort(head)