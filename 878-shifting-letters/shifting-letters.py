class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        pref_shifts=[shifts[-1]]
        rev_shifts = shifts[::-1]
        out = []
        for idx in range(1,len(shifts)) :
            pref_shifts.append(rev_shifts[idx]+pref_shifts[-1])

        pref_shifts = pref_shifts[::-1]
        for idx,char in enumerate(s):
            #normalize to 0-25
            norm_ord= ord(char) - ord('a')
            shifted_ord = (norm_ord + pref_shifts[idx])%26
            out.append(chr(ord('a')+shifted_ord))

        return ''.join(out)