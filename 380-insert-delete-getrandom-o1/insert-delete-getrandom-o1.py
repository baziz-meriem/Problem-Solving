import random
class RandomizedSet:

    def __init__(self):
        self.rand_set = set()


    def insert(self, val: int) -> bool:
        if val in self.rand_set:
            return False
        else:
            self.rand_set.add(val) 
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.rand_set:
            self.rand_set.remove(val)  
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        
        return random.choice(list(self.rand_set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()