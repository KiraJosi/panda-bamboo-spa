import tkinter as tk
from tkinter import messagebox
from spa.data_manager import load_bookings, load_services, load_expenses

class FinanceOverviewWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Finance Overview")
        self.window.geometry("400x400")
        self._build_ui()
        self._calculate_finances()

    def _build_ui(self):
        self.text = tk.Text(self.window, width=50, height=20)
        self.text.pack(pady=10)

    def _calculate_finances(self):
        # 1️⃣ Einnahmen aus Bookings berechnen
        bookings_data = load_bookings()
        services_data = load_services()
        service_prices = {s["name"]: s["price"] for s in services_data}
        total_income = 0
        income_details = []

        for b in bookings_data:
            price = service_prices.get(b["service_name"], 0)
            total_income += price
            income_details.append(f"{b['customer_name']} → {b['service_name']}: €{price}")

        # 2️⃣ Ausgaben laden
        expenses_data = load_expenses()
        total_expenses = sum([e["amount"] for e in expenses_data])
        expense_details = [f"{e['name']}: €{e['amount']}" for e in expenses_data]

        # 3️⃣ Gewinn berechnen
        profit = total_income - total_expenses

        # 4️⃣ Alles anzeigen
        self.text.insert(tk.END, "💰 Einnahmen:\n")
        for line in income_details:
            self.text.insert(tk.END, f"  {line}\n")
        self.text.insert(tk.END, f"Total Income: €{total_income}\n\n")

        self.text.insert(tk.END, "📉 Ausgaben:\n")
        for line in expense_details:
            self.text.insert(tk.END, f"  {line}\n")
        self.text.insert(tk.END, f"Total Expenses: €{total_expenses}\n\n")

        self.text.insert(tk.END, f"📈 Gewinn: €{profit}\n")

