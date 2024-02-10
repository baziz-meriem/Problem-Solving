class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        strings_dict ={val:idx for idx,val in enumerate(list1) }
        solution =[]
        for s,idx in strings_dict.items():
            if s not in list2:
                strings_dict[s] = float('inf')
            else:
                strings_dict[s] += list2.index(s) 

        min_idx = min(strings_dict.values())

        for s,idx in strings_dict.items():
            if idx == min_idx:
                solution.append(s)
        return solution



        