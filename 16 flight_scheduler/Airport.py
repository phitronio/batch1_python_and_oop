class Airport:
    def __init__(self, code, name, city, country, lat, long, rate) -> None:
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.lat = lat
        self.long = long
        self.rate = rate

    def __repr__(self) -> str:
        return f'Airport: {self.name} in: {self.country} lat: {self.lat} long: {self.long} rate: {self.rate}'