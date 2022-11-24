class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = {}
        
        for lst in cpdomains:
            lst = lst.split()
            cnt = lst[0]
            url = lst[1]
            
            word = ""
            
            for w in url.split(".")[::-1]:
                word=w+word
                
                mp[word] = int(cnt)+mp.get(word,0)
                
                word = "."+word
            
        result = []
        
        for k,v in mp.items():
            result.append(str(v)+" "+k)
            
        return result