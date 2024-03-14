class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        s_dict = { car:idx for idx,car in enumerate(s) }
       
        parts_sizes = []
        prev_last_idx = 0
        idx = 0
        last_idx = s_dict[s[0]]
        #iterate through the string
        while idx < len(s):
            print("idx==",idx)
            val = s[idx]

            if idx < last_idx:
                last_idx = max(s_dict[val],last_idx)
                
            elif idx == last_idx:
                
                parts_sizes.append(len(s[prev_last_idx:last_idx+1]))
                prev_last_idx = last_idx+1
                last_idx = s_dict[s[idx+1]] if idx+1<len(s) else s_dict[s[idx]]
            
            
            idx += 1
        return parts_sizes

        

        
