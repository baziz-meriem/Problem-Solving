class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def buildString(n):
            def invert(st):
                return ''.join(["1" if s=="0" else "0" for s in st ])
                
            if n==1:
                return "0"
            else:
                st = buildString(n-1)
                #print("s",n,"is: ", st + "1" +invert(st)[::-1])
                return  st + "1" +''.join(invert(st)[::-1])
            
        return buildString(n)[k-1]