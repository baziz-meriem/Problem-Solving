class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        booked_flights=[0]*n
        flights = []
        for first,last,seats in bookings:
            booked_flights[first-1] += seats
            if last <n:
                booked_flights[last] -= seats
       
            
        return list(accumulate(booked_flights))