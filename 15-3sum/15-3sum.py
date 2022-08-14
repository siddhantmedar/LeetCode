class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)-2):
            x = nums[i]
            
            low, high = i+1, len(nums)-1
            
            while low < high:
                sm = nums[i]+nums[low]+nums[high]
                if sm == 0:
                    lst = [nums[i], nums[low], nums[high]]
                    if lst not in res:
                        res.append(lst)
                    low+=1
                    high-=1
                elif sm > 0:
                    high-=1
                elif sm < 0:
                    low+=1
            
        return res            
        