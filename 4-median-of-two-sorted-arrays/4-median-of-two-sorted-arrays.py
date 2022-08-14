class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        
        if m>n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        low, high = 0, m
        
        while low<=high:
            cut1 = (low+high)//2
            cut2 = int(((m+n+1)/2) - cut1)
            
            l1 = nums1[cut1-1] if cut1 != 0 else float("-inf")
            l2 = nums2[cut2-1] if cut2 != 0 else float("-inf")
            r1 = nums1[cut1] if cut1 != m else float("inf")
            r2 = nums2[cut2] if cut2 != n else float("inf")
        
            if l1<=r2 and l2<=r1:
                if (m+n)%2:
                    return max(l1, l2)
                else:
                    return (max(l1, l2)+min(r1,r2)) / 2
                
            elif l1 > r2:
                high = cut1-1
                
            else:
                low = cut1+1
                
        return 0