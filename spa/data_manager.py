import json
import os
from spa.service import Service
from spa.customer import Customer
from spa.booking import Booking


DATA_FILE = "data/spa_data.json"


def load_services():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("services", [])

def save_services(services: list):
    data = {"services": [s.to_dict() for s in services]}
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_customers():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            data = json.loads(content)
            return data.get("customers", [])
    except json.JSONDecodeError:
        return []

def save_customers(customers: list):
    # Lade bestehenden Content
    existing_data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                try:
                    existing_data = json.loads(content)
                except json.JSONDecodeError:
                    existing_data = {}

    existing_data["customers"] = [c.to_dict() for c in customers]

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=4)
