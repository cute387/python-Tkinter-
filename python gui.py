import tkinter as tk
from tkinter import messagebox

# Coffee menu with prices in INR
menu = {
    "Espresso": 100,
    "Americano": 120,
    "Latte": 150,
    "Cappuccino": 160,
    "Mocha": 180
}

class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Menu")
        self.root.geometry("300x400")
        self.total = 0
        self.selected_items = []

        # Heading
        tk.Label(root, text="Coffee Menu", font=("Arial", 18, "bold")).pack(pady=10)

        # Coffee item buttons
        for coffee, price in menu.items():
            btn = tk.Button(root, text=f"{coffee} - ₹{price}",
                            font=("Arial", 12),
                            command=lambda c=coffee: self.add_item(c))
            btn.pack(pady=5)

        # Total label
        self.total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 14))
        self.total_label.pack(pady=20)

        # Checkout button
        tk.Button(root, text="Checkout", font=("Arial", 12, "bold"), bg="green", fg="white",
                  command=self.checkout).pack(pady=10)

    def add_item(self, coffee):
        price = menu[coffee]
        self.total += price
        self.selected_items.append(coffee)
        self.total_label.config(text=f"Total: ₹{self.total}")

    def checkout(self):
        if not self.selected_items:
            messagebox.showinfo("Checkout", "No items selected.")
            return
        items_str = "\n".join(self.selected_items)
        messagebox.showinfo("Checkout", f"You ordered:\n{items_str}\n\nTotal: ₹{self.total}")
        self.total = 0
        self.selected_items.clear()
        self.total_label.config(text="Total: ₹0")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeApp(root)
    root.mainloop()
