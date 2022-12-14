class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp = {idx:nums[idx] for idx in range(len(nums)) if nums[idx]!=0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        
        for k,v in vec.mp.items():
            if k in self.mp:
                result+=self.mp[k]*v
                
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)