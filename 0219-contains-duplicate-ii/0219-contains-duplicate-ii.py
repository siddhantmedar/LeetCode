class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = defaultdict(list)
        
        for i,ele in enumerate(nums):
            if ele in mp:
                for idx in mp[ele]:
                    if i-idx <= k:
                        return True
            
            mp[ele].append(i)
        
        return False