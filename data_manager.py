import json
from spa.service import Service
from spa.customer import Customer
from spa.booking import Booking


DATA_FILE = "data.json"


def save_data(services, customers, bookings, expenses):
    data = {
        "services": [
            {
                "name": s.name,
                "price": s.price,
                "duration": s.duration_minutes
            } for s in services
        ],
        "customers": [
            {
                "name": c.name,
                "species": c.species
            } for c in customers
        ],
        "bookings": [
            {
                "customer": b.customer.name,
                "service": b.service.name,
                "date_time": b.date_time
            } for b in bookings
        ],
        "expenses": [
            {
                "description": e[0],
                "amount": e[1]
            } for e in expenses
        ]
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return [], [], [], []

    services = [
        Service(s["name"], s["price"], s["duration"])
        for s in data.get("services", [])
    ]

    customers = [
        Customer(c["name"], c["species"])
        for c in data.get("customers", [])
    ]

    service_dict = {s.name: s for s in services}
    customer_dict = {c.name: c for c in customers}

    bookings = []
    for b in data.get("bookings", []):
        customer = customer_dict.get(b["customer"])
        service = service_dict.get(b["service"])
        if customer and service:
            bookings.append(Booking(customer, service, b["date_time"]))

    expenses = [
        (e["description"], e["amount"])
        for e in data.get("expenses", [])
    ]

    return services, customers, bookings, expenses

