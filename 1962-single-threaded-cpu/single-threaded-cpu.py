import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        ind = 0
        for i in tasks:
            i.append(ind)
            ind+=1
        tasks.sort()
        print(tasks)


        heap = []
        i = 0
        arrivalTime = tasks[0][0]
        while(i < n):
            if tasks[i][0] == arrivalTime:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
            else:
                break 
            i+=1

        order = []
        while(heap):
            process = heapq.heappop(heap)
            order.append(process[1])
            arrivalTime += (process[0])

            while(i < n and tasks[i][0] <= arrivalTime):
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i+=1

            if not heap and i < n:
                arrivalTime = tasks[i][0]
                while(i < n):
                    if tasks[i][0] == arrivalTime:
                        heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                    else:
                        break 
                    i+=1

        return order