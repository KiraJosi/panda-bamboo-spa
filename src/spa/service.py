class Service:
    def __init__(self, name: str, price: float, duration: int):
        self.name = name
        self.price = price
        self.duration = duration

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "duration": self.duration
        }

    @staticmethod
    def from_dict(data: dict):
        return Service(
            name=data["name"],
            price=data["price"],
            duration=data["duration"]
        )

