class Solution:
    def largestPalindromic(self, num: str) -> str:
        mp = {int(x):0 for x in sorted(str(num), reverse=True)}
        
        for i in str(num):
            c = int(i)        
            mp[c] = 1+mp.get(c,0)
        
        mid = None
        
        left, right = "", ""
        
        for k,v in mp.items():
            if v%2 == 0:
                for i in range(v//2):
                    left+=str(k)
                    right = str(k)+right

            elif v%2:
                for i in range((v-1)//2):
                    left+=str(k)
                    right = str(k)+right
                
                if mid == None:
                    mid = k
                else:
                    mid = max(mid, k)
                    
        result = None
        
        if mid != None:
            result = left+str(mid)+right
        
        else:
            result = left+right

        i,j = 0, len(result)-1
        
        while i<=j and result[i] == "0" and result[j] == "0":
            i+=1
            j-=1
            
        if i > j:
            return "0"
            
        return result[i:j+1]