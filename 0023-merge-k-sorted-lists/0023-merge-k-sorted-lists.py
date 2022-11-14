# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for lst in lists:
            while lst:
                heap.append(lst.val)
                lst = lst.next
                
        heapq.heapify(heap)
        
        dummy = ListNode(-1)
        tmp = dummy
        
        while heap:
            node = heapq.heappop(heap)
            tmp.next = ListNode(node)
            tmp = tmp.next
            
        return dummy.next