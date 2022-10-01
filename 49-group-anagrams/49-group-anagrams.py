class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for word in strs:
            container = [0]*26
            
            for c in word:
                container[ord(c)-ord('a')]+=1

            mp[tuple(container)].append(word)    
        
        return [v for _,v in mp.items()]