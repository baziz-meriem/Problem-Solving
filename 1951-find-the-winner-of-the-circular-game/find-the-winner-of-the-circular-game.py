class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([element for element in range(1,n+1)])

        while len(q)>1:
            for _ in range(1,k):
                q.append(q.popleft())
            q.popleft()

        return q[0]

