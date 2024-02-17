class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        cap = capacity
        #parcourir la liste
        for idx,water_amount in enumerate(plants):
            steps += 1
            #chaque fois verifier si capacity >= la valeur 
            if cap >= water_amount:
                #incrementé steps by 1
                cap -=water_amount#5-2-->3-2-->1
            else :
                #si non steps += steps*2+1  
                steps = (idx)*2 + steps#7+8--->15
                cap = capacity - water_amount #-->2

        return steps
        