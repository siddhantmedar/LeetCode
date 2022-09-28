class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mp = {}
        
        for ele in nums:
            if not ele%2:
                mp[ele] = 1+mp.get(ele, 0)
                
        heap = [(-v,k) for k,v in mp.items() if not k%2]
        
        if heap:
            heapq.heapify(heap)
            
            return heap[0][1]
        
        else:
            return -1