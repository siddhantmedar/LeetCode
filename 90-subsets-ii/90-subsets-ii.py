class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        
        result = []
        
        nums.sort()
        
        for i in range(2**N):
            tmp = []
            
            for j in range(N):
                if i&(1<<j):
                    tmp.append(nums[j])
                    
            if tmp not in result:
                result.append(tmp)
                
        return result