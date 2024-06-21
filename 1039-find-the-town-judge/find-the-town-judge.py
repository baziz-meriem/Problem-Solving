class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l = [0]*(n+1)
        m = [0]*(n+1)

        for a,b in trust:
            l[a]+=1
            m[b]+=1
        for i in range(1,n+1):
            if l[i]==0 and m[i]==n-1:
                return i
        return -1