class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [nums[0]]
        
        for i, ele in enumerate(nums[1:]):
            idx = bisect.bisect_left(result, ele)
            
            if idx == len(result):
                result.append(ele)
                
            else:
                result[idx] = ele
                
        return len(result)