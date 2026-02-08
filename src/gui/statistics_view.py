import tkinter as tk
from tkinter import messagebox
from collections import Counter
from src.spa.data_manager import load_bookings

# Für Diagramme
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class StatisticsWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Statistics")
        self.window.geometry("600x500")
        self._build_ui()
        self._calculate_statistics()

    def _build_ui(self):
        # Textbereich für Details
        self.text = tk.Text(self.window, width=50, height=10)
        self.text.pack(pady=10)

        # Frame für Diagramm
        self.chart_frame = tk.Frame(self.window)
        self.chart_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    def _calculate_statistics(self):
        bookings_data = load_bookings()
        if not bookings_data:
            self.text.insert(tk.END, "No bookings yet.\n")
            return

        # -----------------------------
        # 1️⃣ Beliebteste Services
        # -----------------------------
        services = [b["service_name"] for b in bookings_data]
        service_counts = Counter(services)
        most_common_services = service_counts.most_common()

        self.text.insert(tk.END, "📊 Most Popular Services:\n")
        for service, count in most_common_services:
            self.text.insert(tk.END, f"  {service}: {count} bookings\n")
        self.text.insert(tk.END, "\n")

        # -----------------------------
        # 2️⃣ Häufigste Kunden
        # -----------------------------
        customers = [b["customer_name"] for b in bookings_data]
        customer_counts = Counter(customers)
        most_common_customers = customer_counts.most_common()

        self.text.insert(tk.END, "🐾 Most Frequent Customers:\n")
        for customer, count in most_common_customers:
            self.text.insert(tk.END, f"  {customer}: {count} bookings\n")
        self.text.insert(tk.END, f"\nTotal Bookings: {len(bookings_data)}\n")

        # -----------------------------
        # 3️⃣ Diagramm für Services
        # -----------------------------
        if most_common_services:
            fig, ax = plt.subplots(figsize=(5,3))
            services_names = [s[0] for s in most_common_services]
            services_values = [s[1] for s in most_common_services]

            ax.barh(services_names, services_values, color='green')
            ax.set_xlabel("Bookings")
            ax.set_title("Bookings per Service")
            ax.invert_yaxis()  # Beliebtester Service oben

            # Diagramm in tkinter Frame einbetten
            canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
