class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def isprice(word):
            return word[0]=="$" and len(word) > 1 and all([c.isdigit() or c=="." for c in word[1:]])
        
        words = sentence.split(" ")
        
        result = []
        
        for word in words:
            if not isprice(word):
                result.append(word)
                
            else:
                amt = int(word[1:])
                dis = "{:.2f}".format(amt*(100-discount)/100)
                result.append("$" + str(dis))
                
        return " ".join(result)