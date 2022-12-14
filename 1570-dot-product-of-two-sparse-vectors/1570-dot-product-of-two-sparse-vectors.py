class SparseVector:
    def __init__(self, nums: List[int]):
        self.lst = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        
        for i in range(len(self.lst)):
            result+=self.lst[i]*vec.lst[i]
            
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)