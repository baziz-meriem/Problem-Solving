from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        car_counter = Counter(s)
        max_heap = [(-freq,car) for car,freq in car_counter.items()]
        heapq.heapify(max_heap)
        result=[]
        prev_freq,prev_car = 0,None

        while max_heap:
            freq,car = heapq.heappop(max_heap)
            result.append(car)

            
            if prev_freq<0:
                heapq.heappush(max_heap,(prev_freq,prev_car))
            prev_freq,prev_car = freq +1 ,car
            

        str_result = ''.join(result)
        return str_result if len(str_result)==len(s) else ''
