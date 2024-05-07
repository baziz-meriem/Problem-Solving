from collections import OrderedDict
 
 
class LRUCache:
    capacity: int
    cache_map: OrderedDict
 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = OrderedDict()
 
    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1
 
        value = self.cache_map[key]
        self.cache_map.move_to_end(key)
 
        return value
 
    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map[key] = value
            self.cache_map.move_to_end(key)
            return
 
        if len(self.cache_map) >= self.capacity:
            lru_key = next(iter(self.cache_map))
            del self.cache_map[lru_key]
 
        self.cache_map[key] = value