class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        mp1, mp2 = dict(), dict()
        
        for i,(a,b) in enumerate(zip(s,t)):
            if a not in mp1 and b not in mp2:
                mp1[a]=b
                mp2[b]=a
            
            else:
                if (a in mp1 and mp1[a]!=b) or (a in mp2 and mp2[a]!=b):
                    return False
                if (b in mp1 and mp1[b]!=a) or (b in mp2 and mp2[b]!=a):
                    return False
                
        return True
    
# b=b b=b
# a=a a=a
# d=b b=d