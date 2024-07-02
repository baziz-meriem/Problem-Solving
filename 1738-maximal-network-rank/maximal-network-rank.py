class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g=[[False]*n for _ in range(n)]
        for x,y in roads:
            g[x][y]=g[y][x]=True

        ans=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue

                cur=0
                for k in range(n):
                    if k!=i and k!=j:
                        if g[i][k]:
                            cur+=1

                        if g[j][k]:
                             cur+=1

                if g[i][j]:
                    cur+=1

                ans=max(cur,ans)

        return ans             