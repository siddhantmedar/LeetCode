class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all([65<=ord(x)<=90 for x in word]) or \
           all([97<=ord(x)<=122 for x in word]) or \
           65<=ord(word[0])<=90 and all([97<=ord(x)<=122 for x in word[1:]]):
            return True
        else:
            return False