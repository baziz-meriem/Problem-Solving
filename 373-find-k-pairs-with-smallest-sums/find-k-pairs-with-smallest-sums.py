import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        # Initialize a min-heap to store the pairs
        heap = []

        # Push the first pair from each row of nums1 into the heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        result = []

        while k > 0 and heap:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            # Push the next pair from the current row of nums1 into the heap
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result