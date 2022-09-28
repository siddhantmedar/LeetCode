class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1, st2 = [], []

        for c in s:
            if c == "#":
                if st1:
                    st1.pop()

            else:
                st1.append(c)

        for c in t:
            if c == "#":
                if st2:
                    st2.pop()

            else:
                st2.append(c)
                
        return "".join(st1) == "".join(st2)