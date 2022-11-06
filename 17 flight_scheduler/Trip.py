class Trip:
    def __init__(self, trip_cities, aircraft, price, start_date, route = '') -> None:
        self.trip_cities = trip_cities
        self.start_date = start_date
        self.aircraft = aircraft
        self.trip_route = route
        self.price = price

    def __repr__(self) -> str:
        # return f'Trip: {self.trip_cities} Aircraft: {self.aircraft} route: {self.trip_route} cost: {self.price}'
        return f'Trip: {self.trip_cities} cost: {self.price}'
    
