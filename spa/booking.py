from datetime import datetime

class Booking:
    def __init__(self, customer_name: str, service_name: str, date_time: str):
        self.customer_name = customer_name
        self.service_name = service_name
        self.date_time = date_time  # Format: "YYYY-MM-DD HH:MM"

    def to_dict(self):
        return {
            "customer_name": self.customer_name,
            "service_name": self.service_name,
            "date_time": self.date_time
        }

    @staticmethod
    def from_dict(data: dict):
        return Booking(
            customer_name=data["customer_name"],
            service_name=data["service_name"],
            date_time=data["date_time"]
        )


