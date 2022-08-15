class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mp1 = Counter(nums1)
        mp2 = Counter(nums2)
        mp3 = Counter(nums3)
        
        st = (set(nums1).union(nums2)).union(nums3)
        
        res = []
        
        for x in st:
            if (x in mp1 and x in mp2 and x in mp3) or \
            ((x in mp1 and x in mp2) or (x in mp2 and x in mp3) or\
             (x in mp1 and x in mp3)):
                res.append(x)
                
        return res