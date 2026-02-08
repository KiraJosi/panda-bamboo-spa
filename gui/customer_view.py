import tkinter as tk
from tkinter import messagebox
from spa.customer import Customer
from spa.data_manager import load_customers, save_customers

class CreateCustomerWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Create Customer")
        self.window.geometry("300x200")
        self._build_ui()

    def _build_ui(self):
        tk.Label(self.window, text="Customer Name").pack(pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        tk.Label(self.window, text="Species").pack(pady=5)
        self.species_entry = tk.Entry(self.window)
        self.species_entry.pack()

        tk.Button(
            self.window,
            text="Save Customer",
            command=self._save_customer
        ).pack(pady=15)

    def _save_customer(self):
        name = self.name_entry.get()
        species = self.species_entry.get()

        if not name or not species:
            messagebox.showerror("Error", "All fields are required.")
            return

        new_customer = Customer(name, species)

        customers_data = load_customers()
        customers = [Customer.from_dict(c) for c in customers_data]
        customers.append(new_customer)
        save_customers(customers)

        messagebox.showinfo("Customer Created", f"Customer '{name}' created successfully!")
        self.window.destroy()

