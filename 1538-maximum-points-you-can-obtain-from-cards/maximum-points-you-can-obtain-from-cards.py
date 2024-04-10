class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints)-k
        
        total_sum = sum(cardPoints)
        min_sum = sum(cardPoints[0:window_size])
        pref_sum=[cardPoints[0]]

        for idx in range(1,len(cardPoints)):
            pref_sum.append(pref_sum[-1]+cardPoints[idx])

        idx = 1
        while idx < len(cardPoints)-window_size+1:
            current_sum = pref_sum[idx+window_size-1] - pref_sum[idx-1]
            min_sum = min(min_sum,current_sum)
            idx += 1
        return total_sum - min_sum