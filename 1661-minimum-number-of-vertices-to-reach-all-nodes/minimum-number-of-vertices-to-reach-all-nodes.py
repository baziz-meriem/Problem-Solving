class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = collections.defaultdict(list)
        result  = []
        for src,dest in edges:
            incoming[dest].append(src)
        print(incoming.items())

        for edge in range(0,n):
            if not incoming[edge]:
                result.append(edge)
        return result