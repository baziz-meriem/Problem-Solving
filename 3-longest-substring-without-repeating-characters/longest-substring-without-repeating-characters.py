class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        s_dict = {}
        l = 0

        for _,val in enumerate(s):

            if val not in s_dict.keys():
                s_dict[val] = 1         

            else:                        
                while val in s_dict.keys():
                    s_dict[s[l]] -= 1
                    if  s_dict[s[l]] == 0 :
                        del  s_dict[s[l]]
                    l += 1
                s_dict[val] = 1
            max_len = len(s_dict.keys()) if len(s_dict.keys())> max_len else max_len
            

        return max_len