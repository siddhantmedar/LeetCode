class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not low%2:
            low+=1
            
        return 0 if high < low else ((high-low)//2)+1