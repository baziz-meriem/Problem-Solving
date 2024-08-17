from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(val):
            res=[]
            for i in range(4):
                child1= val[:i] + str((int(val[i])+1) %10) + val[i+1:]
                child2= val[:i] + str((int(val[i])-1+10) %10) + val[i+1:]
                res.append(child1)
                res.append(child2)
            return res
            
        
        visited=set(deadends)
        q = deque()
        q.append(["0000",0])
        while q :
            val,moves = q.popleft()
            if val == target:
                return moves
            for child in children(val):
                if child not in visited:
                    visited.add(child)
                    q.append([child,moves+1])
        return -1