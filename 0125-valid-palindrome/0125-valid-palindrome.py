class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(word):
            low, high = 0, len(word)-1
            
            while low < high:
                if word[low] != word[high]:
                    return False
                
                low+=1
                high-=1
                
            return True
            
            
        text = ""
        
        for c in s:
            if c.isalnum():
                text+=c.lower()

        # print(text)
        
        return check(text)