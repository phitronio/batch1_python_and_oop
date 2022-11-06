from All_Airports import AllAirports
from Air_Lines import AirLines
from Trip import Trip
from itertools import permutations


class TravelAgent:
    def __init__(self, name) -> None:
        self.name = name
        self.trips = None
        self.all_airports = AllAirports()
        self.air_lines = AirLines()
    '''
        params: 
        start: starting city Code
        end: destination city code
        start_date: date when you want to start the trip

        return: 
        aircraft, price

        notes: use airlines to select aircraft
    '''
    def set_trip_one_city_one_way(self, start, end, start_date):
        price = self.all_airports.get_ticket_price(start, end)
        distance = self.all_airports.distance_between_two_airports(start, end)
        aircraft = self.air_lines.get_aircraft_by_distance(distance)
        trip = Trip([start, end], aircraft, price, start_date, [start, end] )
        return trip
    
    '''
        trip_info: [city0, city1, city2]
    '''
    def set_trip_one_city_round_way(self, start, end, start_date):
        trip1 = self.set_trip_one_city_one_way(start, end, start_date)
        trip2 = self.set_trip_one_city_one_way(end, start, start_date)
        return [trip1, trip2]

    '''
        trip_info: [city0, city1, city2]
    '''
    def set_trip_two_city_one_way(self, trip_info, start_date):
        trip1 = self.set_trip_one_city_one_way(trip_info[0], trip_info[1], start_date)
        trip2 = self.set_trip_one_city_one_way(trip_info[1], trip_info[2], start_date)
        return [trip1, trip2]

    '''
        trip_info: [city0, city1, city2, city3, city4]
    '''
    def set_trip_multi_city_one_way_fixed_route(self, trip_info, start_date):
        trips = []
        for i in range(0, len(trip_info)-1):
            trip = self.set_trip_one_city_one_way(trip_info[i], trip_info[i + 1], start_date)
            trips.append(trip)
        return trips

    '''
        trip_info: [city0, city1, city2, city3, city4]
    '''
    def set_trip_multi_city_flexible_route(self, trip_cities, start_date):
        start_city = trip_cities[0]
        flexible_cities = trip_cities[1:]
        
        for sequence in permutations(flexible_cities):
            print(sequence)
            # DUB ('LHR', 'SYD', 'JFK')
            cities = [start_city] + list(sequence)
            print(cities)
            # for i in range(0, len(flexible_cities)):
                

    
    def __repr__(self) -> str:
        return f'TravelAgent: {self.name}'