# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            pre, curr = None, head
            
            while curr:
                ref = curr.next
                curr.next = pre
                pre = curr
                curr = ref
                
            return pre
            
            
        dummy = ListNode(-1)
        
        ptr = dummy
        tmp = head
        
        while tmp:
            count = 0
            
            hd = tmp
            
            while tmp:
                count+=1
                if count == k:
                    break
            
                tmp = tmp.next
            
            if count == k:
                ref = tmp.next
                
                tmp.next = None
                
                rev = reverse(hd)
                
                ptr.next = rev
                
                while ptr.next:
                    ptr = ptr.next
                
                tmp = ref
            
            else:
                ptr.next =  hd
                
        return dummy.next
                