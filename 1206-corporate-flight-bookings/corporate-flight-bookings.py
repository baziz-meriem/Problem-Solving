class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        booked_flights=[0]*n
        flights = []
        for first,last,seats in bookings:
            booked_flights[first-1] += seats
            if last <n:
                booked_flights[last] -= seats
       
        #print(booked_flights)
        for idx in range(len(booked_flights)):
            if idx>0:
                booked_flights[idx] += booked_flights[idx-1]  
            
        #print(booked_flights)
        for seats in booked_flights:
            flights.append(seats)
        return flights