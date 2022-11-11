class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(low, high):
            if low <= high:
                mid = (low+high) >> 1
            
                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    return search(mid+1, high)

                else:
                    return search(low,mid-1)
            else:
                return -1
            
        return search(0, len(nums)-1)