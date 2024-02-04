class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        added_letter = ''
        dict_s = {}
        dict_t = {}

        for char in s:
            if char in dict_s.keys():
                dict_s [char] += 1 #{a:1}

            else:
                dict_s [char] = 1 

        for char in t:
            if char in dict_t.keys() :
                dict_t[char] += 1 #{a:2}
                
            else: dict_t[char] = 1   


        if dict_s.keys() == dict_t.keys() :
            for key in dict_t.keys():
                if dict_t[key] != dict_s[key]:
                    added_letter = key
                    break;

        else:
            for key_t in dict_t.keys():
                if key_t not in dict_s.keys() :
                    added_letter = key_t
                    break;


        return added_letter