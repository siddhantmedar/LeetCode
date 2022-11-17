class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(2**len(nums)):
            mask = 1
            tmp = []
            
            for j in range(len(nums)):
                if i & mask > 0:
                    tmp.append(nums[j])
                    
                mask<<=1
                
            result.append(tmp)
            
        return result