class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        
        result = []
        
        for ele in nums[:k]:
            while q and q[-1] < ele:
                q.pop()
            q.append(ele)
            
        result.append(q[0])
        
        for i in range(k,len(nums)):
            # remove
            if q[0] == nums[i-k]:
                q.popleft()
            
            while q and q[-1] < nums[i]:
                q.pop()
            
            q.append(nums[i])
            
            result.append(q[0])
            
        return result