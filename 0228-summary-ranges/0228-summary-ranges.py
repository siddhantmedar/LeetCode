class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        st = set([x for x in nums])
        s,e = None, None
        
        res = []
        
        for i,ele in enumerate(nums):
            if s==None:
                s=ele
                
            if ele+1 not in st:
                e=ele
                if s!=e:
                    res.append(str(s)+"->"+str(e))
                else:
                    res.append(str(s))
                s,e = None, None
                
        return res
                    
            