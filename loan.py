import tkinter as tk
from tkinter import messagebox

def calculate_payment():
    try:
        loan_amount = float(loan_amount_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100
        loan_term = int(loan_term_entry.get())

        monthly_interest_rate = interest_rate / 12
        total_payments = loan_term * 12

        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)

        result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
window=tk.Tk()
window.title("Calculation Tool")
window.geometry("1000x500")
window.config(bg="#fe4d57")


# heading

tk.Label(window,text="Loan Calculator",font="times 30 underline",bg="#fe4d57").pack()

# Create the loan amount input
loan_amount_label = tk.Label(window, text="Loan Amount ($):",bg="#fe4d57", font="arial 20")
loan_amount_label.place(x=150,y=80)
loan_amount_entry = tk.Entry(window, width=30, font="arial 20")
loan_amount_entry.place(x=450,y=80)

# Create the interest rate input
interest_rate_label = tk.Label(window, text="Interest Rate (%):",bg="#fe4d57", font="arial 20")
interest_rate_label.place(x=150,y=140)
interest_rate_entry = tk.Entry(window, width=30, font="arial 20")
interest_rate_entry.place(x=450,y=140)

# Create the loan term input
loan_term_label = tk.Label(window, text="Loan Term (years):", bg="#fe4d57", font="arial 20")
loan_term_label.place(x=150,y=200)
loan_term_entry = tk.Entry(window, width=30, font="arial 20")
loan_term_entry.place(x=450,y=200)

# Create the calculate button
calculate_button = tk.Button(window,bg="#fecd53",font="arial 20", text="Calculate", command=calculate_payment)
calculate_button.place(x=500,y=250)

# Create the result label
result_label = tk.Label(window, text="",bg="#fe4d57",fg="white", font="arial 20")
result_label.place(x=250,y=330)

# Start the Tkinter event loop
window.mainloop()
