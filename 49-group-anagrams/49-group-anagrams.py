class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for word in strs:
            box = [0]*26
            
            for c in word:
                box[ord(c)-ord('a')]+=1
            
            mp[tuple(box)].append(word)
        
        result = []
        
        for k,v in mp.items():
            result.append(v)
            
        return result
            
        