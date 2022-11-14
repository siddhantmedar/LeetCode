class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        
        for ele in nums:
            xor^=ele
        
        mask = 1
        
        while mask&xor == 0:
            mask<<=1
        
        g1, g2 = 0,0
        
        for ele in nums:
            if ele&mask > 0:
                g1^=ele
            else:
                g2^=ele
        
        return [g1,g2]