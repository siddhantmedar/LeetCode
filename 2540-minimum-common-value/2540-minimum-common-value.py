class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx1, idx2 = 0,0
        
        res = float("inf")
        
        while idx1<len(nums1) and idx2<len(nums2):
            if nums1[idx1] == nums2[idx2]:
                res = min(res,nums1[idx1])
                idx1+=1
            else:
                if nums1[idx1] <= nums2[idx2]:
                    idx1+=1
                else:
                    idx2+=1
                    
        return res if res!=float("inf") else -1