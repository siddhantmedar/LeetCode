class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = defaultdict(set)
        
        for i,ele in enumerate(nums):
            if ele in mp:
                for idx in mp[ele]:
                    if i-idx <= k:
                        return True
            
            mp[ele].add(i)
        
        return False