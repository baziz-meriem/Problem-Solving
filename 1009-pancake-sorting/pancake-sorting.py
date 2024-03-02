class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        max_num_idx = -1
        end_idx =len(arr)
        flips = []
        while end_idx != 0:
            max_num = max(arr[:end_idx])
            max_num_idx = arr.index(max_num)
            print("index of the max",max_num_idx)

            arr = arr[:max_num_idx+1][::-1] + arr[max_num_idx+1:]
            flips.append(max_num_idx+1)
            print(f"K={max_num_idx+1}",arr)

            arr = arr[:end_idx][::-1]+arr[end_idx:]
            flips.append(len(arr[:end_idx]))

            print(f"K={len(arr[:end_idx])}",arr)
            end_idx -=1
        return flips
