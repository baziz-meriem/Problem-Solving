class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref_list=[0]*len(s)
        for start,end,direction in shifts:
            dir_num = 1 if direction else -1
            pref_list[start] += dir_num 
            if end+1<len(s):
                pref_list[end+1] -= dir_num
        #propagation
        for idx in range(1,len(pref_list)):
            pref_list[idx] += pref_list[idx-1]

        output = []
        for char,inc in zip(s,pref_list):
            inc_value = (ord(char) - ord('a') + inc) % 26
            ord_ = ord('a') + inc_value
            output.append(chr(ord_))

        return ''.join(output)