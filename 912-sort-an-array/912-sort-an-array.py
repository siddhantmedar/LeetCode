class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lst1 = [0]*(max([abs(x) for x in nums])+1)
        lst2 = [0]*(max([abs(x) for x in nums])+1)
        
        for ele in nums:
            if ele < 0:
                lst2[-1*ele]+=1
            else:
                lst1[ele]+=1
            
        res = []
        
        for i, count in reversed(list(enumerate(lst2))):
            while count:
                res.append(-1*i)
                count-=1
                
        
        for i, count in enumerate(lst1):
            while count:
                res.append(i)
                count-=1
        
        return res