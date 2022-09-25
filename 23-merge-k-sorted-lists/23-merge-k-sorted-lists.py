# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Pair:
    def __init__(self, val, lst):
        self.val = val
        self.lst = lst
        
    def __lt__(self, other):
        if self.val < other.val or self.lst.val < other.lst.val:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.val == other.val and self.lst.val == other.lst.val:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.val > other.val or self.lst.val > other.lst.val:
            return True
        else:
            return False
        
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for list in lists:
            if list:
                heapq.heappush(heap, Pair(list.val, list))
        
        heapq.heapify(heap)
        
        dummy = ListNode(-1)
        tmp = dummy
        
        while heap:
            p = heapq.heappop(heap)
            
            val, node = p.val, p.lst
            
            tmp.next = ListNode(val)
            tmp = tmp.next
            tmp.next = None
                
            node = node.next
            
            if node:
                heapq.heappush(heap, Pair(node.val, node))
        
        return dummy.next