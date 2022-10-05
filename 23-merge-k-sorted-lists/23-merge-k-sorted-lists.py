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
        if self.val < other.val:
            return True
        
    def __gt__(self, other):
        if self.val > other.val:
            return True
        
    def __eq__(self, other):
        if self.val == other.val:
            return True

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for lst in lists:
            if lst:
                heapq.heappush(heap, Pair(lst.val, lst))
                
        heapq.heapify(heap)
        
        dummy = ListNode(-1)
        tmp = dummy
        
        while heap:
            p = heapq.heappop(heap)
            
            val, lst = p.val, p.lst
            
            tmp.next = ListNode(val)
            tmp = tmp.next
            
            lst = lst.next
            
            if lst:
                heapq.heappush(heap, Pair(lst.val, lst))
                
        return dummy.next