# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            if not head or not head.next:
                return head
            
            res = reverse(head.next)
            
            head.next.next = head
            head.next = None
            
            return res
        
        dummy = ListNode(-1)
        tmp2 = dummy
        
        tmp = head
        
        while tmp:
            left = tmp
            count = k
            
            while tmp and count:
                count-=1
                if count == 0:
                    break
                tmp = tmp.next
                
            if count == 0:
                ref = tmp.next
                tmp.next = None
                
                hd = reverse(left)
                
                tmp2.next = hd
                
                while tmp2.next:
                    tmp2 = tmp2.next
                
                tmp = ref
                
            else:
                tmp2.next = left
                
        return dummy.next
                
            