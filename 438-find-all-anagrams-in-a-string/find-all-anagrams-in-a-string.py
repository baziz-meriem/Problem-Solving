from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        p = Counter(p)
        pointer = 0
        current_dict = {}
        output = []
        if window> len(s):
            return []
        for idx in range(window):
            if s[idx] in current_dict.keys():
                current_dict[s[idx]] += 1
            else:
                current_dict[s[idx]] = 1
        if current_dict == p:
                output.append(0)
        for idx in range(1,len(s) - window+1):
            current_dict[s[idx-1]] -= 1

            if s[idx + window-1] in current_dict.keys():
                current_dict[s[idx + window-1]] += 1
            else:
                current_dict[s[idx + window-1]] = 1

            
            current_dict = { key:val for key,val in current_dict.items() if val!=0 }
            #print(current_dict)
            if current_dict == p:
                output.append(idx)

        return output


