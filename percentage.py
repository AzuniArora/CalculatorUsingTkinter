import tkinter as tk
from tkinter import messagebox

def calculate_percentage():
    try:
        base_value = float(base_value_entry.get())
        percentage = float(percentage_entry.get())

        result = (base_value * percentage) / 100

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
window = tk.Tk()
window.title("Percentage Calculator")
window.geometry("1000x500")
window.config(bg="#fe4d57")


#heading
tk.Label(window,text="Percentage Calculator",font="times 30 underline",bg="#fe4d57").pack()
# Create the base value input
base_value_label = tk.Label(window, text="Base Value:",bg="#fe4d57", font="arial 20")
base_value_label.place(x=150,y=80)
base_value_entry = tk.Entry(window,width=30, font="arial 20")
base_value_entry.place(x=350,y=80)

# Create the percentage input
percentage_label = tk.Label(window, text="Percentage (%):",bg="#fe4d57", font="arial 20")
percentage_label.place(x=150,y=140)
percentage_entry = tk.Entry(window,width=30, font="arial 20")
percentage_entry.place(x=350,y=140)

# Create the calculate button
calculate_button = tk.Button(window, bg="#fecd53",font="arial 20",text="Calculate", command=calculate_percentage)
calculate_button.place(x=500,y=200)

# Create the result label
result_label = tk.Label(window, text="",bg="#fe4d57", font="arial 20")
result_label.place(x=150,y=250)

# Start the Tkinter event loop
window.mainloop()

