import tkinter as tk

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

        tk.Button(self.root, text="Create Service").pack(pady=5)
        tk.Button(self.root, text="Create Customer").pack(pady=5)
        tk.Button(self.root, text="Book Appointment").pack(pady=5)
        tk.Button(self.root, text="Finance Overview").pack(pady=5)
        tk.Button(self.root, text="Statistics").pack(pady=5)

    def run(self):
        self.root.mainloop()

