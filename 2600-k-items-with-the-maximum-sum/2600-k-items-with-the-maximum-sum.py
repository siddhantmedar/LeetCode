class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ones = min(numOnes,k)
        k-=ones
        
        if k>0:
            zeros = min(numZeros,k)
            k-=zeros
        
        if k>0:
            return ones-k
        
        return ones