class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        a,b = len(costs)//2,len(costs)//2
        greedyCosts = sorted(costs,key=lambda tup:abs(tup[0]-tup[1]),reverse=True)
        totalCost = 0
        print(greedyCosts)
        for item in greedyCosts:
            if a and b:
                if item[0]<item[1]:
                    a -= 1 
                    totalCost += item[0]
                else:
                    b -= 1
                    totalCost += item[1]
            else:
                if a:
                    totalCost += item[0]
                    a -= 1
                else:
                    totalCost += item[1]
                    b -= 1
        return totalCost

        
        