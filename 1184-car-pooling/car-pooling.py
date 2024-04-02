class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_loc = min(trips, key=lambda x:x[1])[1]
        max_loc = max(trips, key=lambda x: x[-1])[-1]
        
        pref_list= [0 for _ in range(min_loc,max_loc+1)]

        for numPassengers, frm, to in trips:
            pref_list[frm-min_loc] += numPassengers
            pref_list[to-min_loc] -= numPassengers
        
        for  idx in range(len(pref_list)):
            if idx!=0:
                pref_list[idx] += pref_list[idx-1]
            if pref_list[idx] > capacity:
                return False
        return True