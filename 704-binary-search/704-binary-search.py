class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start, end):
            if start <= end:
                mid = (start+end)>>1

                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    return binarySearch(start, mid-1)
                
                else:
                    return binarySearch(mid+1, end)
                
            return -1
        
        return binarySearch(0, len(nums)-1)