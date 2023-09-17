class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt=0
        
        lst = list(combinations(nums,4))
        
        for a,b,c,d in lst:
            if a+b+c==d:
                cnt+=1
                
        return cnt
    
#         for j in range(len(nums)-3):

#             # three ptr + curr
#             for i in range(j+1,len(nums)-2):

#                 # two ptr + curr
#                 l,r = i+1,len(nums)-1

#                 while l<r:
#                     if nums[j] == nums[i] + nums[l] + nums[r]:
#                         print(nums[j],nums[i],nums[l],nums[r])
#                         # result.add((nums[i],nums[l],nums[r],nums[j]))
#                         cnt+=1
#                         l+=1

#                     elif nums[j] < nums[i] + nums[l] + nums[r]:
#                         l+=1

#                     else:
#                         r-=1

#         return cnt