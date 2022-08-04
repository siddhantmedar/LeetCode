class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def isScrambled(x, y):
            if len(x) != len(y):
                return False

            if (not len(x)) or (x == y):
                return True

            if sorted(x) != sorted(y):
                return False

            key = x + y
            if key in dp:
                return dp[key]

            for i in range(1, len(x)):
                if (isScrambled(x[:i], y[:i]) and isScrambled(x[i:], y[i:])) or \
                        (isScrambled(x[-i:], y[:i]) and isScrambled(x[:-i], y[i:])):
                    dp[key] = True
                    return True

            dp[key] = False
            return False


        dp = {}
        
        return isScrambled(s1, s2)
        