class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        if len(nums) == 4:
            return [[ele for ele in nums]] if sum(nums)==target else []
        
        nums.sort()
        
        result = set()
        
        for j in range(len(nums)-3):
            # if j-1>=0 and nums[j]==nums[j-1]:
            #     continue
            
            # three ptr + curr
            for i in range(j+1,len(nums)-2):
                # if i-1>=0 and nums[i]==nums[i-1]:
                #     continue

                # two ptr + curr
                l,r = i+1,len(nums)-1

                while l<r:
                    sm = nums[j] + nums[i] + nums[l] + nums[r]
                    # print(nums[j],nums[i],nums[l],nums[r],sm,target)
                    if sm==target and len(set([j,i,l,r]))==4:
                        result.add((nums[j],nums[i],nums[l],nums[r]))
                        l+=1

                    elif sm < target:
                        l+=1

                    else:
                        r-=1

        return list(result)