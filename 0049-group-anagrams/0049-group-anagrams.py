class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for ele in strs:
            hash = [0]*26
            for c in ele:
                hash[ord(c)-ord('a')]+=1 
                
            mp[tuple(hash)].append(ele)
            
        return [v for k,v in mp.items()]