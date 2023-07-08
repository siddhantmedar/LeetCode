class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for word in strs:
            key = [0]*26
            
            for c in word:
                key[ord(c)-ord('a')]+=1
                
            mp[tuple(key)].append(word)
            
            
        return [word_list for _, word_list in mp.items()]