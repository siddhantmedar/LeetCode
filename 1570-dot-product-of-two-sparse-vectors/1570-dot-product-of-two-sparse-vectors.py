class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp = {}
        
        for i,ele in enumerate(nums):
            if ele:
                self.mp[i] = ele

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        
        for k,v in vec.mp.items():
            if k in self.mp:
                res+=self.mp[k]*v
                
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)