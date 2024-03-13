class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def pal(s):
            return s==s[::-1]

        def pali(x,y):
            l=0
            r=len(x)-1
            while l<r:
                if x[l]==y[r]:
                    l+=1
                    r-=1
                else:
                    if pal(y[l:r+1]) or pal(x[l:r+1]):
                        break
                    return False
            return True
        return pali(a,b) or pali(b,a)