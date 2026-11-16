
import tkinter as tk
from tkinter import messagebox


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x570")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.expenses = []

        # Application title
        tk.Label(
            root,
            text="Expense Tracker",
            font=("Arial", 20, "bold"),
            bg="#f5f5f5"
        ).pack(pady=20)

        # Expense category
        tk.Label(
            root,
            text="Expense Category",
            font=("Arial", 11),
            bg="#f5f5f5"
        ).pack()

        self.category_entry = tk.Entry(
            root,
            width=30,
            font=("Arial", 11)
        )
        self.category_entry.pack(pady=8, ipady=4)

        # Expense amount
        tk.Label(
            root,
            text="Expense Amount (₹)",
            font=("Arial", 11),
            bg="#f5f5f5"
        ).pack()

        self.amount_entry = tk.Entry(
            root,
            width=30,
            font=("Arial", 11)
        )
        self.amount_entry.pack(pady=8, ipady=4)

        # Add expense button
        tk.Button(
            root,
            text="Add Expense",
            command=self.add_expense,
            width=20,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(pady=12)

        # Expense list heading
        tk.Label(
            root,
            text="Expense List",
            font=("Arial", 13, "bold"),
            bg="#f5f5f5"
        ).pack(pady=5)

        # Expense list
        self.expense_list = tk.Listbox(
            root,
            width=40,
            height=10,
            font=("Arial", 10)
        )
        self.expense_list.pack(pady=5)

        # Final total
        self.total_label = tk.Label(
            root,
            text="Final Total: ₹0.00",
            font=("Arial", 13, "bold"),
            bg="#f5f5f5"
        )
        self.total_label.pack(pady=15)

        # Show final total button
        tk.Button(
            root,
            text="Show Final Total",
            command=self.show_total,
            width=20,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(pady=5)

    def add_expense(self):
        category = self.category_entry.get().strip()
        amount_text = self.amount_entry.get().strip()

        # Validate category
        if not category:
            messagebox.showerror(
                "Input Error",
                "Please enter an expense category."
            )
            return

        # Validate amount
        try:
            amount = float(amount_text)

            if amount <= 0:
                messagebox.showerror(
                    "Input Error",
                    "Amount must be greater than zero."
                )
                return

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter a valid numeric amount."
            )
            return

        # Store expense
        self.expenses.append({
            "category": category.title(),
            "amount": amount
        })

        # Update expense list
        self.expense_list.insert(
            tk.END,
            f"{category.title()} - ₹{amount:.2f}"
        )

        # Update total immediately
        self.update_total()

        # Clear input fields
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.focus_set()

    def update_total(self):
        total = sum(item["amount"] for item in self.expenses)

        self.total_label.config(
            text=f"Final Total: ₹{total:.2f}"
        )

    def show_total(self):
        total = sum(item["amount"] for item in self.expenses)

        messagebox.showinfo(
            "Expense Summary",
            f"Number of expenses: {len(self.expenses)}\n"
            f"Final Total: ₹{total:.2f}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
