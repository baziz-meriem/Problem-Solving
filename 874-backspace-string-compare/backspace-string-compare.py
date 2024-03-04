class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def rem_(st: str):
            while '#' in st:
                a = st.index('#')
                if a == 0:
                    st = st[1:]
                else:
                    st = st[:a-1] + st[a+1:]
            return st
        
        s, t = rem_(s), rem_(t)
        return s == t