class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        i = 0
        result = 0
        mp = defaultdict()
        
        for j in range(len(s)):
            ele = s[j]
            
            if ele in mp or (ele not in mp and len(mp) < k):
                mp[ele] = 1+mp.get(ele, 0)
                
            else:
                result = max(result, j-i)
                
                while mp and len(mp) >= k:
                    mp[s[i]]-=1

                    if mp[s[i]] == 0:
                        del mp[s[i]]

                    i+=1

                mp[ele] = 1+mp.get(ele, 0)
        
        if len(mp) <= k:
            result = max(result, len(s)-i)
        
        print(result)
        
        return result
        