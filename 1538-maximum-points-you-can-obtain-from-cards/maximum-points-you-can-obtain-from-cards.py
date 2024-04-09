class Solution:
    def maxScore(self, cardPoints: List[int], K: int) -> int:
        N, S = len(cardPoints), sum(cardPoints)
        wind = ans = sum(cardPoints[:N-K])

        for right in range(N-K,N):
            wind = wind - cardPoints[right - N + K] + cardPoints[right]
            ans = min(ans,wind)
        
        return S - ans