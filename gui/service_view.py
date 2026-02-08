import tkinter as tk
from tkinter import messagebox

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

        tk.Button(
            self.window,
            text="Save Service",
            command=self._save_service
        ).pack(pady=15)

    def _save_service(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        duration = self.duration_entry.get()

        if not name or not price or not duration:
            messagebox.showerror("Error", "All fields are required.")
            return

        # TEMPORARY: later we connect this to the service logic
        messagebox.showinfo(
            "Service Created",
            f"Service '{name}' created successfully!"
        )

        self.window.destroy()

