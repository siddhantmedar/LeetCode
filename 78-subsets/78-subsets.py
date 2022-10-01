class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        N = len(nums)
        
        for i in range(0, 2**N):
            tmp = []
            
            for j in range(N):
                if i & (1<<j) > 0:
                    tmp.append(nums[j])
                    
            result.append(tmp)
        
        return result