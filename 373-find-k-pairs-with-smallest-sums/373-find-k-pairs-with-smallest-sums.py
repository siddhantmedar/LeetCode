class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        result = []
        
        visited = set()
        
        heapq.heappush(heap,(nums1[0]+nums2[0], 0, 0))
        visited.add((0,0))
        
        while heap and k:
            sm, idx1, idx2 = heapq.heappop(heap)
            
            result.append([nums1[idx1], nums2[idx2]])
            
            if idx1+1 < len(nums1) and (idx1+1, idx2) not in visited:
                heapq.heappush(heap, (nums1[idx1+1]+nums2[idx2], idx1+1, idx2))
                visited.add((idx1+1, idx2))
                
            if idx2+1 < len(nums2) and (idx1, idx2+1) not in visited:
                heapq.heappush(heap, (nums1[idx1]+nums2[idx2+1], idx1, idx2+1))
                visited.add((idx1, idx2+1))
                
            k-=1
            
        return result