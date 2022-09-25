# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a < other.a:
            return True
        elif self.a > other.a:
            return False
        elif self.b.val < other.b.val:
            return True
        elif self.b.val > other.b.val:
            return False

    def __eq__(self, other):
        return self.a == other.a and self.b.val == other.b.val

    def __gt__(self, other):
        if self.a > other.a:
            return True
        elif self.a < other.a:
            return False
        elif self.b.val > other.b.val:
            return True
        elif self.b.val < other.b.val:
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
            
            val, node = p.a, p.b
            
            tmp.next = ListNode(val)
            tmp = tmp.next
            tmp.next = None
                
            node = node.next
            
            if node:
                heapq.heappush(heap, Pair(node.val, node))
        
        return dummy.next