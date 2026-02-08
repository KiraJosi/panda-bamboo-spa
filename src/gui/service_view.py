import tkinter as tk
from tkinter import messagebox
from src.spa.service import Service
from src.spa.data_manager import load_services, save_services

class CreateServiceWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Create Service")
        self.window.geometry("300x250")
        self._build_ui()

    def _build_ui(self):
        tk.Label(self.window, text="Service Name").pack(pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        tk.Label(self.window, text="Price (€)").pack(pady=5)
        self.price_entry = tk.Entry(self.window)
        self.price_entry.pack()

        tk.Label(self.window, text="Duration (min)").pack(pady=5)
        self.duration_entry = tk.Entry(self.window)
        self.duration_entry.pack()

        tk.Button(self.window, text="Save Service", command=self._save_service).pack(pady=15)

    def _save_service(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        duration = self.duration_entry.get()

        if not name or not price or not duration:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            price = float(price)
            duration = int(duration)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number and duration must be an integer.")
            return

        # 1️⃣ Service erstellen
        new_service = Service(name, price, duration)

        # 2️⃣ Services laden, anhängen, speichern
        services_data = load_services()
        services = [Service.from_dict(s) for s in services_data]
        services.append(new_service)
        save_services(services)

        messagebox.showinfo("Service Created", f"Service '{name}' created successfully!")
        self.window.destroy()
