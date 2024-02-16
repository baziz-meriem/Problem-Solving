class OrderedStream:
    
    def __init__(self, n: int):
        self.n = n
        self.stream_dict = defaultdict(int)


    def insert(self, idKey: int, value: str) -> List[str]:
        chunk =[]
        self.stream_dict[idKey] = value
        if idKey==1 or self.stream_dict[idKey-1] == -1:#if Im the first element or the element before me is already printed
            
            while self.stream_dict[idKey] != 0:
                
                chunk.append(self.stream_dict[idKey])
                self.stream_dict[idKey]  = -1 #to indicate that it was already appended
                idKey += 1

        return chunk
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)