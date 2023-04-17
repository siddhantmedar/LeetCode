class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def compute_pi(p):
            pi = [0]*len(p)
            
            j=0
            
            for i in range(1,len(p)):
                while j>0 and p[i]!=p[j]:
                    j=pi[j-1]
                    
                if p[i]==p[j]:
                    j+=1
                    
                pi[i]=j
                
            return pi
            
            
        def kmp(t,p):
            pi = compute_pi(p)
            m,n = len(t), len(p)
            
            i,j = 0,0
            
            while i<m:
                if t[i]==p[j]:
                    i+=1
                    j+=1
                    if j==n:
                        return i-n
                
                elif j>0:
                    j = pi[j-1]
                
                else:
                    i+=1
            
            return -1
            
            
        res = set()
        seen = set()
        
        for t in words:
            for p in words:
                if t==p or (t,p) in seen:
                    continue
                
                if len(p) < len(t):
                    seen.add((t,p))
                    if kmp(t,p) >= 0:
                        res.add(p)
                        
        return list(res)