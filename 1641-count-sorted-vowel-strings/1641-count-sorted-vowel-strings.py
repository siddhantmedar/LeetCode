class Solution:
    def countVowelStrings(self, n: int) -> int:
        def solve(idx,path,ln):
            nonlocal mp, cnt
            
            if ln == 0:
                cnt+=1
                return
            
            for i in range(idx,len(mp)):
                path+=mp[i]
                solve(i,path,ln-1)    
        
        
        mp = {0:"a", 1:"e", 2:"i", 3:"o", 4:"u"}
        cnt = 0
        
        solve(0,"",n)
        
        return cnt
        
        """
        a e i o u
        """