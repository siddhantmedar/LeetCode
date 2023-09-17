class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        if len(nums) == 3:
            return [[ele for ele in nums]] if sum(nums)==0 else []
        
        nums.sort()
        
        result = set()
        
        for i in range(len(nums)-2):
            if i-1>=0 and nums[i]==nums[i-1]:
                continue
            
            # two ptr + curr
            l,r = i+1,len(nums)-1
            
            while l<r:
                sm = nums[i] + nums[l] + nums[r]

                if sm==0 and (i!=l and l!=r and i!=r):
                    result.add((nums[i],nums[l],nums[r]))
                    l+=1

                elif sm < 0:
                    l+=1

                else:
                    r-=1
        
        return list(result)