from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.travel_dict = defaultdict(lambda:[0,0])
        self.checkin_dict = defaultdict(lambda:("",0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_dict[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_stationName,start_time = self.checkin_dict[id]
        del self.checkin_dict[id]
        self.travel_dict[(start_stationName,stationName)][0] += t - start_time
        self.travel_dict[(start_stationName,stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        total_travel_time =  self.travel_dict[(startStation,endStation)][0]
        total_passengers =  self.travel_dict[(startStation,endStation)][1]

        return total_travel_time/total_passengers
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)