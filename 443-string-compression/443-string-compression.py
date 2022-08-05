class Solution:
    def compress(self, nums: List[str]) -> int:
        i = 0
        
        pre = nums[0]
        count = 1
        
        for j in range(1, len(nums)):
            curr = nums[j]
            
            if curr != pre:
                nums[i] = pre
                i+=1
                
                if count > 1:
                    tmp = str(count)

                    for c in tmp:
                        nums[i] = c
                        i+=1

                pre = curr
                count = 1
                
            elif curr == pre:
                count+=1
        
        nums[i] = pre
        i+=1
        
        if count > 1:
            tmp = str(count)

            for c in tmp:
                nums[i] = c
                i+=1

        return i
    
        