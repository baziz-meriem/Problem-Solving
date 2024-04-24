from collections import deque
class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:

        prev_t = self.requests[0] if self.requests else float('inf')
        diff = t - prev_t
        self.requests.append(t)

        while diff > 3000 and self.requests:
            
            self.requests.popleft()
            if self.requests:
                prev_t = self.requests[0]
                diff = t - prev_t

            
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)