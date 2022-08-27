class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        
        mp = {}
        
        for i in range(len(nums2)):
            ele = nums2[i]
            
            while st and nums2[st[-1]] < ele:
                idx = st.pop()
                mp[nums2[idx]] = ele
                
            st.append(i)
            
        while st:
            idx = st.pop()
            mp[nums2[idx]] = -1
        
        res = []
        
        for ele in nums1:
            res.append(mp[ele])
            
        return res