class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        strings_dict = {val: idx for idx, val in enumerate(list1)}
        min_idx = float('inf')
        result = []

        for s, idx in strings_dict.items():
            if s in list2:
                combined_idx = idx + list2.index(s)
                if combined_idx < min_idx:
                    min_idx = combined_idx
                    result = [s]
                elif combined_idx == min_idx:
                    result.append(s)

        return result
