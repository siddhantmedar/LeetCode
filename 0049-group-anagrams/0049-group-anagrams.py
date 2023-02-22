class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for word in strs:
            ch = [0]*26
            
            for c in word:
                ch[ord(c)-ord('a')]+=1
            
            mp[tuple(ch)].append(word)
            
        return [v for k,v in mp.items()]