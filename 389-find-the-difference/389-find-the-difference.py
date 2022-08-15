class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
#         mp = {}
#         res = None
        
#         for c in s:
#             mp[c] = 1+mp.get(c,0)
            
#         for c in t:
#             if c in mp:
#                 mp[c]-=1
#             else:
#                 res = c
        
#         for k,v in mp.items():
#             if v:
#                 res = k
        
        res = 0
        
        for c in s:
            res^=ord(c)
        
        for c in t:
            res^=ord(c)
            
        return chr(res)
        return res
            
        