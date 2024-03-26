class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_len = 0
        l = 0  
        t = 0  
        target = "aeiou"

        for r in range(len(word)):
            if r > 0 and word[r] < word[r-1]:
                l = r  
                t = 0  

            if word[r] == target[t]:  
                if t == 4:  
                    max_len = max(max_len, r-l+1)
                else:
                    t += 1  

            elif word[r] != target[max(t-1, 0)]:  
                l = r + 1  
                t = 0  

        return max_len
