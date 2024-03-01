from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([i for i in range(1,n+1)])
        while len(q)>1:
            for i in range(1,k):
                q.rotate(-1)
                
            q.popleft()
        return q[0]

