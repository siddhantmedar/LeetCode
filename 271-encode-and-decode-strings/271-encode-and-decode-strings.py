class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        
        for s in strs:
            result+=s
            result+="]][["
        
        return result[:-4]
        
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = s.split("]][[")
        
        # print(result)
        
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))