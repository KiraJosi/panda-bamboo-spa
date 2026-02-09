import tkinter as tk
from tkinter import messagebox
from src.spa.data_manager import load_customers, load_services, load_bookings, save_bookings
from src.spa.booking import Booking
from datetime import datetime

class CreateBookingWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Create Booking")
        self.window.geometry("350x300")
        self._build_ui()

    def _build_ui(self):
        tk.Label(self.window, text="Select Customer").pack(pady=5)
        customers_data = load_customers()
        self.customers = [c["name"] for c in customers_data]
        self.customer_var = tk.StringVar(value=self.customers[0] if self.customers else "")
        self.customer_menu = tk.OptionMenu(self.window, self.customer_var, *self.customers)
        self.customer_menu.pack()

        tk.Label(self.window, text="Select Service").pack(pady=5)
        services_data = load_services()
        self.services = [s["name"] for s in services_data]
        self.service_var = tk.StringVar(value=self.services[0] if self.services else "")
        self.service_menu = tk.OptionMenu(self.window, self.service_var, *self.services)
        self.service_menu.pack()

        tk.Label(self.window, text="Date & Time (YYYY-MM-DD HH:MM)").pack(pady=5)
        self.datetime_entry = tk.Entry(self.window)
        self.datetime_entry.pack()

        tk.Button(
            self.window,
            text="Save Booking",
            command=self._save_booking
        ).pack(pady=15)

    def _save_booking(self):
        customer = self.customer_var.get()
        service = self.service_var.get()
        date_time = self.datetime_entry.get()

        if not customer or not service or not date_time:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Date must be in format YYYY-MM-DD HH:MM")
            return

        new_booking = Booking(customer, service, date_time)

        bookings_data = load_bookings()
        bookings = [Booking.from_dict(b) for b in bookings_data]
        bookings.append(new_booking)
        save_bookings(bookings)

        # Einnahmen automatisch berechnen
        services_data = load_services()
        price = next((s["price"] for s in services_data if s["name"] == service), 0)
        messagebox.showinfo("Booking Created", f"Booking saved!\nRevenue: €{price}")

        self.window.destroy()

