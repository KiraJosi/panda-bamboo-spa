import tkinter as tk
from gui.service_view import CreateServiceWindow
from gui.customer_view import CreateCustomerWindow
from gui.booking_view import CreateBookingWindow
from gui.finance_view import FinanceOverviewWindow
from gui.expenses_view import ExpensesWindow

class PandaSpaApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PandaSpa 🐼🌿")
        self.root.geometry("400x350")

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self.root,
            text="Welcome to PandaSpa",
            font=("Arial", 16)
        )
        title.pack(pady=20)

        tk.Button(
            self.root,
            text="Create Service",
            command=self._open_create_service
        ).pack(pady=5)
        tk.Button(
            self.root,
            text="Create Customer",
            command=self._open_create_customer
        ).pack(pady=5)
        tk.Button(
            self.root,
            text="Book Appointment",
            command=self._open_create_booking
        ).pack(pady=5)
        tk.Button(
            self.root,
            text="Manage Expenses",
            command=self._open_expenses
        ).pack(pady=5)
        tk.Button(
            self.root,
            text="Finance Overview",
            command=self._open_finance_overview
        ).pack(pady=5)
        tk.Button(self.root, text="Statistics").pack(pady=5)


    def _open_create_service(self):
        CreateServiceWindow(self.root)


    def _open_create_customer(self):
        CreateCustomerWindow(self.root)


    def _open_create_booking(self):
        CreateBookingWindow(self.root)


    def _open_finance_overview(self):
        FinanceOverviewWindow(self.root)


    def _open_expenses(self):
        ExpensesWindow(self.root)


    def run(self):
        self.root.mainloop()

