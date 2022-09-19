class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        st = set()
        
        for ele in nums:
            if ele in st:
                return True
            
            st.add(ele)
            
        return False 
        '''
        
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            
        return False