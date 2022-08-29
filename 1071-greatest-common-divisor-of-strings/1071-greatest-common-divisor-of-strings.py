class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
            if len(str1) < len(str2):
                return self.gcdOfStrings(str2, str1)

            elif str1[:len(str2)] != str2:
                return ""

            elif not str2:
                return str1

            else:
                return self.gcdOfStrings(str1[len(str2):], str2)
        