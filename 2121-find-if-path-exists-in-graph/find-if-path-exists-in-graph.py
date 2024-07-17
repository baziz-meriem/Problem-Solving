class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def rec(node,g,vis):
            vis[node]=1
            for i in g[node]:
                if not vis[i]:
                    rec(i,g,vis)
        g=[[] for _ in range(n)]
        for i in edges:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])
        vis=[0 for i in range(n)]
        rec(source,g,vis)
        return vis[destination]