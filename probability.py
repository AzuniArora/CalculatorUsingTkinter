import tkinter as tk
from tkinter import messagebox

def calculate_probability():
    try:
        total_outcomes = float(total_outcomes_entry.get())
        favorable_outcomes = float(favorable_outcomes_entry.get())

        probability = favorable_outcomes / total_outcomes

        result_label.config(text=f"Probability: {probability:.4f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
window=tk.Tk()
window.title("Calculation Tool")
window.geometry("900x500")
window.config(bg="#fe4d57")


# heading

tk.Label(window,text="Probability Calculator",font="times 30 underline",bg="#fe4d57").pack(pady=40)


# Create the total outcomes input
total_outcomes_label = tk.Label(window, text="Total Outcomes:",bg="#fe4d57", font="arial 20")
total_outcomes_label.place(x=50,y=100)
total_outcomes_entry = tk.Entry(window,width=30, font="arial 20")
total_outcomes_entry.place(x=310,y=100)

# Create the favorable outcomes input
favorable_outcomes_label = tk.Label(window, text="Favorable Outcomes:" ,bg="#fe4d57", font="arial 20")
favorable_outcomes_label.place(x=50,y=160)
favorable_outcomes_entry = tk.Entry(window,width=30, font="arial 20")
favorable_outcomes_entry.place(x=310,y=160)

# Create the calculate button
calculate_button = tk.Button(window,bg="#fecd53",font="arial 20", text="Calculate", command=calculate_probability)
calculate_button.place(x=500,y=240)

# Create the result label
result_label = tk.Label(window, text="",bg="#fe4d57", font="arial 20")
result_label.place(x=150,y=300)

# Start the Tkinter event loop
window.mainloop()
