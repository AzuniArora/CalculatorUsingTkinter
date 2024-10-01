import tkinter as tk
from tkinter import messagebox

def calculate_total():
    try:
        purchase_amount = float(purchase_amount_entry.get())
        tax_rate = float(tax_rate_entry.get()) / 100

        total_amount = purchase_amount + (purchase_amount * tax_rate)

        result_label.config(text=f"Total Amount: ${total_amount:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
window=tk.Tk()
window.title("Calculation Tool")
window.geometry("900x500")
window.config(bg="#fe4d57")


# heading

tk.Label(window,text="Sales Tax Calculator",font="times 30 underline",bg="#fe4d57").pack(pady=40)


# Create the purchase amount input
purchase_amount_label = tk.Label(window, text="Purchase Amount ($):",bg="#fe4d57", font="arial 20")
purchase_amount_label.place(x=60,y=100)
purchase_amount_entry = tk.Entry(window,width=30, font="arial 20")
purchase_amount_entry.place(x=350,y=100)

# Create the tax rate input
tax_rate_label = tk.Label(window, text="Tax Rate (%):",bg="#fe4d57", font="arial 20")
tax_rate_label.place(x=60,y=160)
tax_rate_entry = tk.Entry(window,width=30, font="arial 20")
tax_rate_entry.place(x=350,y=160)

# Create the calculate button
calculate_button = tk.Button(window,bg="#fecd53",font="arial 20", text="Calculate", command=calculate_total)
calculate_button.place(x=500,y=220)

# Create the result label
result_label = tk.Label(window, text="",bg="#fe4d57",fg="white", font="arial 20")
result_label.place(x=150,y=260)

# Start the Tkinter event loop
window.mainloop()
