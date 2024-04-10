class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dict_count={"T":0,"F":0}
        left=0
        max_consecutive=0
        max_count=0

        for right in range(len(answerKey)) :
            dict_count[answerKey[right]] += 1
            max_count = max(max_count,dict_count[answerKey[right]])

            if (right-left+1 - max_count )>k:
                    dict_count[answerKey[left]] -= 1
                    left += 1
            max_consecutive = max(max_consecutive, right-left+1 )
        return max_consecutive
