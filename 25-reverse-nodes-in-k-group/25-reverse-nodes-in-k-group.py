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
        tmp = dummy
        
        ptr = head
        
        while ptr:
            count = 0
            ptr = head
            
            while count != k and ptr:
                count+=1
                
                if count == k:
                    break
                    
                ptr = ptr.next
                
            if count == k:
                ref = ptr.next if ptr else None
                ptr.next = None
                revHead = reverse(head)
                tmp.next = revHead
                
                while tmp.next:
                    tmp = tmp.next
                    
                head = ref
            
            else:
                tmp.next = head
        
        return dummy.next
                    
                
                
                