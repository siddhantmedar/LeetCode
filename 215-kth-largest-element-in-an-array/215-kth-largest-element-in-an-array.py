class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l,r):
            pivot = nums[r]
            p = l
            
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
                    
            nums[p], nums[r] = nums[r], nums[p]
            
            if p == K:
                return nums[p]
            
            elif p > K:
                return quickSelect(l,p-1)
            
            elif p < K:
                return quickSelect(p+1,r)
            
        K = len(nums)-k
        return quickSelect(0,len(nums)-1)
    
    # 1 2 3 4 5 6
    