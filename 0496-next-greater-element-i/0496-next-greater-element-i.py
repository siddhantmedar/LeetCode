class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = dict()
        st = []
        res = [-1]*len(nums2)
        
        for i in range(len(nums2)-1,-1,-1):
            if not st:
                res[i]=-1
            
            while st and not st[-1] > nums2[i]:
                st.pop()
                
            if st:
                res[i] = st[-1]
            
            st.append(nums2[i])
            
        for i,ele in enumerate(nums2):
            mp[ele] = res[i]
            
        return [mp[ele] for ele in nums1]
            