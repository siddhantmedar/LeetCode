class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()
        
        for i in range(k):
            if not q:
                q.append(nums[i])
                
            else:
                while q and q[-1] < nums[i]:
                    q.pop()
                
                q.append(nums[i])
                
        result.append(q[0])
        
        for i in range(k, len(nums)):
            if nums[i-k] == q[0]:
                q.popleft()
                
            while q and q[-1] < nums[i]:
                q.pop()
                
            q.append(nums[i])
            
            result.append(q[0])
            
        return result
        