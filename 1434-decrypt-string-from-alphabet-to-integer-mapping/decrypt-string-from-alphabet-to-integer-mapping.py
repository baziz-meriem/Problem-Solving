class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26,0,-1):
            s = s.replace(str(i)+"#", chr(ord("a")+i-1)) if i>9 else s.replace(str(i), chr(ord("a")+i-1))
        return s


    
        