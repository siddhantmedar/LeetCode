class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(str1, str2):
            if len(str1) < len(str2):
                return gcd(str2, str1)

            elif str1[:len(str2)] != str2:
                return ""

            elif not str2:
                return str1

            else:
                return gcd(str1[len(str2):], str2)
            
        return gcd(str1, str2)
        