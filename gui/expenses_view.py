import tkinter as tk
from tkinter import messagebox
from spa.data_manager import load_expenses, save_expenses

class ExpensesWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Manage Expenses")
        self.window.geometry("350x300")
        self._build_ui()
        self._load_expenses()

    def _build_ui(self):
        # Liste der aktuellen Ausgaben
        tk.Label(self.window, text="Current Expenses:").pack(pady=5)
        self.expense_listbox = tk.Listbox(self.window, width=40)
        self.expense_listbox.pack()

        # Neue Ausgabe hinzufügen
        tk.Label(self.window, text="Expense Name").pack(pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        tk.Label(self.window, text="Amount (€)").pack(pady=5)
        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack()

        tk.Button(
            self.window,
            text="Add Expense",
            command=self._add_expense
        ).pack(pady=10)

    def _load_expenses(self):
        """Lädt Ausgaben aus JSON und zeigt sie in der Listbox an"""
        self.expenses = load_expenses()
        self.expense_listbox.delete(0, tk.END)
        for e in self.expenses:
            self.expense_listbox.insert(tk.END, f"{e['name']}: €{e['amount']}")

    def _add_expense(self):
        name = self.name_entry.get().strip()
        amount_text = self.amount_entry.get().strip()

        if not name or not amount_text:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        new_expense = {"name": name, "amount": amount}
        self.expenses.append(new_expense)
        save_expenses(self.expenses)

        # Liste aktualisieren
        self._load_expenses()
        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        messagebox.showinfo("Expense Added", f"Added expense '{name}' (€{amount})")

