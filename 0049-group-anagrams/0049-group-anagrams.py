class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for word in strs:
            box = [0 for _ in range(26)]
            for c in word:
                box[ord(c)-ord('a')]+=1
                
            mp[tuple(box)].append(word)
            
        return [v for v in mp.values()]