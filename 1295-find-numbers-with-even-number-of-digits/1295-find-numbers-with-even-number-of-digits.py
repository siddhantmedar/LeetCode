class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for ele in nums:
            res = int(math.floor(math.log10(ele)+1))
            
            if res % 2 == 0:
                count+=1
                
        return count