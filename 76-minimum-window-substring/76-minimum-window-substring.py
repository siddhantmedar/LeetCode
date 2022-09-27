class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = dict()
        
        for c in t:
            ref[c] = 1+ref.get(c,0)
        
        need = len(ref)
        mp = dict()
        result = float("inf")
        answer = None
        
        i = 0
        
        for j, c in enumerate(s):
            if c in ref:
                mp[c] = 1 + mp.get(c, 0)
                if mp[c] == ref[c]:
                    need-=1
                    
                    if need == 0:
                        while need == 0:
                            if j-i+1 < result:
                                result = j-i+1
                                answer = s[i:j+1]
                                
                            if s[i] in ref:
                                mp[s[i]]-=1
                                
                                if mp[s[i]] < ref[s[i]]:
                                    need+=1
                            else:
                                mp[s[i]]-=1
                                
                            i+=1
            else:
                mp[c] = 1+mp.get(c, 0)
                
        if need == 0:
            if len(s)-i < result:
                result = len(s)-i
                answer = s[i:]
            
        print(result)
        
        return answer if answer else ""