class Solution:
    def nextGreaterElement(self, n: int) -> int:
        lst = [int(x) for x in str(n)]
        
        idx = None
        
        for i in range(len(lst)-2,-1,-1):
            if lst[i] >= lst[i+1]:
                continue
            else:
                idx = i
                break
        
        #descending order
        if idx == None:
            return -1
        
        cand = None
        for i in range(idx+1, len(lst)):
            if lst[i] > lst[idx]:
                if not cand or (cand and lst[i] < lst[cand]):
                    cand = i
                
        lst[idx], lst[cand] = lst[cand], lst[idx]
        
        lst = lst[:idx+1]+sorted(lst[idx+1:])
        
        res = int("".join([str(x) for x in lst]))
        
        return res if -2**31<=res<=2**31-1 else -1
        