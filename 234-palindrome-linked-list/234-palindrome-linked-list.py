# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def isPalin():
            start, end = 0, len(lst)-1
            
            while start < end:
                if lst[start] != lst[end]:
                    return False
                
                start+=1
                end-=1
                
            return True
        
        
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
        
        return isPalin()