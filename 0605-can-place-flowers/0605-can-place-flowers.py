class Solution:
    def canPlaceFlowers(self, lst: List[int], n: int) -> bool:
        lst = [0]+lst+[0]
        
        for i in range(1,len(lst)-1):
            if lst[i]==0 and lst[i-1]==0 and lst[i+1]==0:
                lst[i]=1
                n-=1
                
        return n<=0
        
        # _ 0 0 1 0 1 0 1 0 0 1 _
        
        [0,1,0,1,0,0,1,0]
2

[0,1,0,1,0,0,0]
1