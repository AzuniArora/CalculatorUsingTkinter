import tkinter as tk
from tkinter import messagebox

def calculate_fee():
    try:
        transaction_amount = float(transaction_amount_entry.get())

        fee_percentage = 2.9  # PayPal transaction fee percentage
        fixed_fee = 0.3  # PayPal fixed transaction fee

        fee = (transaction_amount * fee_percentage / 100) + fixed_fee

        result_label.config(text=f"PayPal Fee: ${fee:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

# Create the main window
window=tk.Tk()
window.title("Calculation Tool")
window.geometry("900x500")
window.config(bg="#fe4d57")


# heading

tk.Label(window,text="PayPal Fee  Calculator",font="times 30 underline",bg="#fe4d57").pack(pady=40)


# Create the transaction amount input
transaction_amount_label = tk.Label(window, text="Transaction Amount ($):",bg="#fe4d57", font="arial 20")
transaction_amount_label.pack()
transaction_amount_entry = tk.Entry(window,width=30, font="arial 20")
transaction_amount_entry.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate",bg="#fecd53",font="arial 20", command=calculate_fee)
calculate_button.pack(pady=20)

# Create the result label
result_label = tk.Label(window, text="",bg="#fe4d57", font="arial 20")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
