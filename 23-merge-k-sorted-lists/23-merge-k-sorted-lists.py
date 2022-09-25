# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for list in lists:
            while list:
                heap.append(list.val)
                list = list.next
                
        heapq.heapify(heap)
        
        dummy = ListNode(-1)
        tmp = dummy
        
        while heap:
            val = heapq.heappop(heap)
            
            tmp.next = ListNode(val)
            tmp = tmp.next
                
        return dummy.next