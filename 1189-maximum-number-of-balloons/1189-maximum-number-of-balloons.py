class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = {c:0 for c in "balon"}
        
        for c in text:
            if c in mp:
                mp[c]+=1
                
        mp["l"]//=2
        mp["o"]//=2
        
        if len(mp) < 5:
            return 0
        
        return min([v for k,v in mp.items()])