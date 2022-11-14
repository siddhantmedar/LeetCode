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
        return True if self.val < other.val else False
    def __eq__(self, other):
        return True if self.val == other.val else False    
    def __gt__(self, other):
        return True if self.val > other.val else False
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for lst in lists:
            if lst:
                heap.append(Pair(lst.val, lst))
        
        heapq.heapify(heap)
        
        dummy = ListNode(-1)
        tmp = dummy
        
        while heap:
            node = heapq.heappop(heap)
            tmp.next = ListNode(node.val)
            tmp = tmp.next
            
            node.lst = node.lst.next
            
            if node.lst:
                heapq.heappush(heap,Pair(node.lst.val, node.lst))
            
        return dummy.next