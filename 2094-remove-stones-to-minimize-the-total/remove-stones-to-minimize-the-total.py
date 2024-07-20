import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-pile for pile in piles]
        heapq.heapify(maxHeap)
        
        for _ in range(k):
            pile = -heapq.heappop(maxHeap)
            pile -= pile//2
            heapq.heappush(maxHeap,-pile)

        total_sum = -sum(maxHeap)
        return total_sum